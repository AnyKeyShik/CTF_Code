#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from math import pow


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)


def gen_key(modulo):
    key = randint(pow(10, 20), modulo)
    while gcd(modulo, key) != 1:
        key = randint(pow(10, 20), modulo)

    return key


def power(num, exp, mod):
    x = 1
    y = num

    while exp > 0:
        if exp % 2 != 0:
            x = (x * y) % mod
        y = (y * y) % mod

        exp = exp // 2

    return x % mod


def encrypt(flag, modulo, generator, pub):
    sender_key = gen_key(modulo)
    secret = power(pub, sender_key, modulo)
    c1 = power(generator, sender_key, modulo)
    c2 = secret * flag

    return c1, c2


def decrypt(c1, c2, priv, modulo):
    c1_x = power(c1, priv, modulo)
    msg = (c2 // c1_x) % modulo
    msg = hex(msg)[2:]
    msg = ''.join([chr(int(''.join(ch), 16)) for ch in zip(msg[0::2], msg[1::2])])

    return msg


def read_flag():
    with open("flag", 'r') as flagfile:
        flag = flagfile.read()

    hexflag = "".join("{:02x}".format(ord(ch)) for ch in flag)
    numflag = int(hexflag, 16)

    return numflag


def prepare_elgamal():
    modulo = randint(pow(10, 20), pow(10, 50))
    generator = randint(2, modulo)
    private = gen_key(modulo)
    public = power(generator, private, modulo)

    return (modulo, generator, public), private


def main():
    # Challenge text
    CHALL_TEXT = "Hi. This is your friendly 'Decryption Oracle'\nWe have implemented a well-known public-key cryptosystem. Guess which ;)\n\nModulo: {modulo}\nGenerator: {generator}\nPublic key: {public}\nCiphertext: {cipher}\n\nInsert your Ciphertext-Tuple for me to decrypt - comma seperated (e.g. 5,6)"
    SAME_MSG = "Duh! This would be too easy, right?"
    INVITE = ">>> "
    INCORRECT_INPUT = "Incorrect input!"

    flag = read_flag()

    public, private = prepare_elgamal()
    cipher = encrypt(flag, *public)

    print(CHALL_TEXT.format(modulo=public[0], generator=public[1], public=public[2], cipher=cipher))

    while True:
        print(INVITE, end='')
        user_input = input()

        try:
            enc_msg = tuple(map(int, user_input.split(', ')))

            if len(enc_msg) != 2:
                raise ValueException
        except Exception:
            print(INCORRECT_INPUT)
            continue

        if enc_msg == cipher:
            msg = SAME_MSG
        else:
            msg = decrypt(*enc_msg, private, public[0])

        print(msg)


if __name__ == '__main__':
    main()
