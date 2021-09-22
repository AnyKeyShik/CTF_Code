#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from base64 import b64decode
from Crypto.Cipher import AES
from secretsharing import SecretSharer


if len(sys.argv) < 4:
    print("Usage: {} part1 part2 part2".format(sys.argv[0]))
    exit(1)

AES_KEY = SecretSharer.recover_secret([sys.argv[1], sys.argv[2], sys.argv[3]])
IV = b'\x00' * 16
cipher = AES.new(key=AES_KEY, mode=AES.MODE_CBC, iv=IV)

with open('flag.enc', 'r') as flagfile:
    enc_flag = b64decode(flagfile.read())

flag = cipher.decrypt(enc_flag)

print("Decrypted flag is: {}".format(flag))
