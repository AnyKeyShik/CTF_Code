#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from base64 import b64encode

with open('key', 'r') as key:
    AES_KEY = bytes(key.read(), encoding='utf-8')
with open('iv', 'rb') as key:
    IV = key.read()

cipher = AES.new(key=AES_KEY, mode=AES.MODE_CBC, iv=IV)

with open('flag', 'r') as flagfile:
    flag = bytes(flagfile.read(), encoding='utf-8')

enc_flag = cipher.encrypt(flag)

with open('flag.enc', 'w') as flagfile:
    flagfile.write(b64encode(enc_flag).decode('utf-8'))
