#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hashlib import sha1

SALT = "so salty, so cute:3 CTF Code 2021"
STARTING_STRING = '''
do you know that md5 of "oren_ctf" is cfe721641130ac5151d3c55fd8121ece?
'''

some_hash = sha1(STARTING_STRING.encode()).hexdigest()
for i in range(99):
    some_hash = sha1((some_hash + SALT).encode()).hexdigest()

print(some_hash)
