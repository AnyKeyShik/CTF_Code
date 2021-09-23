#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
from secretsharing import SecretSharer


def main():
    # Number of secret shards
    SHARDS = 5

    # Number of shards what will be send to user
    SEND_SHARDS = 3

    # Challenge text
    CHALL_TEXT = "Here's a base64-encoded and encrypted flag: {flag}\nYou need a secret and literally zero ivent to get it!\n\nIt's your three part:"

    # Get encrypted flag
    with open('flag.enc', 'r') as flagfile:
        CHALL_TEXT = CHALL_TEXT.format(flag=flagfile.read())

    # Get AES key
    with open('key', 'r') as key:
        AES_KEY = key.read()

    shares = SecretSharer.split_secret(AES_KEY, SEND_SHARDS, SHARDS)

    print(CHALL_TEXT)
    for i in range(SEND_SHARDS):
        current_part = i + 1
        print("Part {part_num}: {part}".format(part_num=current_part, part=shares[i]))


if __name__ == "__main__":
    main()
