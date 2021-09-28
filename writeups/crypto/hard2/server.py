#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
import random
import ecc
import cryptor


def readline(sock):
    buffer = ''

    while True:
        data = sock.recv(1)

        if not data:
            raise RuntimeError
        if data == '\n':
            break

        buffer += data

    return buffer


def sendline(sock, buffer):
    buffer += '\n'
    sock.send(buffer)


def readpoint(sock):
    buffer = readline(sock).split(',')

    if len(buffer) != 2:
        raise RuntimeError

    x = buffer[0]
    y = buffer[1]

    return int(x), int(y)


def sendpoint(sock, x, y):
    sendline(sock, '{},{}'.format(x, y))


def sendcurve(sock, a, b, p):
    sendline(sock, '{},{},{}'.format(a, b, p))


def recv_connection(conn):
    curves = [
        [[23749, 409741011, 426546346592070269], [729,28539]],
        [[9326, 1376127157, 354990952970600489], [4093588398, 494204038]],
        [[30800, 1187016249, 546422503250358263], [1146878855, 243009781]],
        [[16057, 421810025, 322083043555692967], [2478569373, 360426459]],
        [[32593, 1864507527, 560147175803221327], [2309607047, 53492280]]
    ]

    random.seed('F1ut5chF1ng3r5')
    d = random.randint(2, 2 ** 56)

    scratch = random.randint(5, 50)
    curve_index = scratch % 5
    priv_key = d + scratch

    a = curves[curve_index][0][0]
    b = curves[curve_index][0][1]
    p = curves[curve_index][0][2]
    prim_x = curves[curve_index][1][0]
    prim_y = curves[curve_index][1][1]

    try:
        sendline(conn, "Establishing secure connection via ECDH...")
        sendcurve(conn, a, b, p)
        sendpoint(conn, prim_x, prim_y)

        sendline(conn, "Accept? [y/n]")
        confirm = readline(conn).lower()
        if confirm == 'n':
            sendline(conn, "Waiting for point")
            prim_x, prim_y = readpoint(conn)
        elif confirm == 'y':
            pass
        else:
            sendline(conn, "Illegal response, aborting...")
            raise RuntimeError

        if not ecc.is_point_on_curve(prim_x, prim_y, a, b, p):
            sendline(conn, "Illegal point, aborting...")
            raise RuntimeError

        server_x, server_y = ecc.point_mul(prim_x, prim_y, priv_key, a, p)
        sendpoint(conn, server_x, server_y)

        client_x, client_y = readpoint(conn)
        if not ecc.is_point_on_curve(client_x, client_y, a, b, p):
            sendline(conn, "Illegal point, aborting...")
            raise RuntimeError

        priv_x, priv_y = ecc.point_mul(client_x, client_y, priv_key, a, p)

        cipher = cryptor.cryptor(priv_x, priv_y, "server")

        sendline(conn, cipher.encrypt("Successfully established the secure connection"))
        sendline(conn, cipher.encrypt("Waiting for operator to jump in"))

        msg = ""
        while msg.lower() != "bye":
            print cipher.decrypt(readline(conn))
            msg = raw_input("Message: ")
            sendline(conn, cipher.encrypt(msg))

    except RuntimeError:
        print "Something went wrong. Please contact to Dr. Evil via drevil@totallynotevil.die"

    finally:
        conn.close()


def main():
    HOST = ''
    PORT = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    try:
        while True:
            conn, addr = sock.accept()
            print "Incoming connection from {}:{}".format(addr[0], addr[1])
            recv_connection(conn)

    finally:
        sock.close()


if __name__ == "__main__":
    main()

