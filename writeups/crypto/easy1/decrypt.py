#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base65536
import pybase100 as base100
import base64


def decode(flag):
    flag = base65536.decode(flag)
    flag = base100.decode(flag)
    flag = base64.b64decode(flag)
    flag = flag.decode('utf-8')

    return flag

def main():
    with open("flag.enc", 'r') as flag_file:
        flag = flag_file.read()

    print(decode(flag))


if __name__ == '__main__':
    main()
