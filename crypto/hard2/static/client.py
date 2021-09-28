#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
import time
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


def readcurve(sock):
    buffer = readline(sock).split(',')

    if len(buffer) != 3:
        raise RuntimeError

    a = buffer[0]
    b = buffer[1]
    p = buffer[2]

    return int(a), int(b), int(p)


def main():
    PORT = 5000

    ip = raw_input("Server: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, PORT))

    try:
        print readline(sock)

        a, b, p = readcurve(sock)
        prim_x, prim_y = readpoint(sock)

        print readline(sock)
        confirm = raw_input()
        sendline(sock, confirm)

        d = random.randint(2, 2 ** 56)

        client_x, client_y = ecc.point_mul(prim_x, prim_y, d, a, p)
        sendpoint(sock, client_x, client_y)

        server_x, server_y = readpoint(sock)
        priv_x, priv_y = ecc.point_mul(server_x, server_y, d, a, p)

        cipher = cryptor.cryptor(priv_x, priv_y, "client")

        print cipher.decrypt(readline(sock))
        print cipher.decrypt(readline(sock))

        msg = ""
        while msg.lower() != "bye":
            msg = raw_input("Message: ")
            sendline(sock, cipher.encrypt(msg))
            print cipher.decrypt(readline(sock))

    except RuntimeError:
        print "Something went wrong. Please contact to Dr. Evil via drevil@totallynotevil.die"

    finally:
        sock.close()


if __name__ == "__main__":
    main()

