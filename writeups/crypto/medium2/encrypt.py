#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from base64 import b64encode


def prepare_cipher(key_file, iv_file):
    with open(key_file, 'r') as key, open(iv_file, 'rb') as iv:
        AES_KEY = bytes(key.read(), encoding='utf-8')
        IV = iv.read()

    return AES.new(key=AES_KEY, mode=AES.MODE_CBC, iv=IV)


def main():
    with open("flag", 'r') as flagfile:
        flag = bytes(flagfile.read(), encoding='utf-8')

    cipher = prepare_cipher("key", "iv")
    enc_flag = cipher.encrypt(flag)

    with open("flag.enc", 'w') as flagfile:
        flagfile.write(b64encode(enc_flag).decode('utf-8'))


if __name__ == '__main__':
    main()
