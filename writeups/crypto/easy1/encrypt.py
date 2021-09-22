#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base65536
import pybase100 as base100
import base64


def encode(flag):
    flag = flag.encode('utf-8')
    flag = base64.b64encode(flag)
    flag = base100.encode(flag)
    flag = base65536.encode(flag)

    return flag


def main():
    with open("flag", 'r') as flagfile, open("flag.enc", 'w') as enc_flagfile:
        flag = flagfile.read()
        enc_flag = encode(flag)
        enc_flagfile.write(enc_flag)


if __name__ == '__main__':
    main()
