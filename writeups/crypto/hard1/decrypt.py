#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *
import re


def get_cipher(msg):
    str_tp = re.search(r'\d*, \d*', msg).group(0)

    return tuple(map(int, str_tp.split(', ')))


def mul_tuple(tuple):
    new_tuple = (tuple[0], tuple[1] * 2)

    return  ', '.join(map(str, new_tuple))


def get_decrypt_flag(enc_flag):
    hexflag2 = ''.join('{:02x}'.format(ord(ch)) for ch in enc_flag)
    numflag2 = int(hexflag2, 16)
    numflag = numflag2 // 2
    hexflag = hex(numflag)[2:]

    return ''.join([chr(int(''.join(ch), 16)) for ch in zip(hexflag[0::2], hexflag[1::2])])


def main():
    r = remote('localhost', 1488)

    msg = r.recvuntil('>>> ').decode('utf-8')
    tuple = get_cipher(msg)

    msg_for_flag = mul_tuple(tuple)
    r.sendline(msg_for_flag)

    enc_flag = r.recvline().decode('utf-8')
    flag = get_decrypt_flag(enc_flag)

    print("Decrypted flag: {}".format(flag))

    r.close()


if __name__ == '__main__':
    main()
