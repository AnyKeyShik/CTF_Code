#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
from secretsharing import SecretSharer

# Server address
SERVER_ADDRESS = ('', 1488)

# Number of secret shards
SHARDS = 5

# Number of shards what will be send to user
SEND_SHARDS = 3

# Challenge text
CHALL_TEXT = "Here's a base64-encoded and encrypted flag: {flag}\nYou need a secret and literally zero ivent to get it!\n\nIt's your three part:\n"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(50)

    # Get encrypted flag
    with open('flag.enc', 'r') as flagfile:
        CHALL_TEXT = CHALL_TEXT.format(flag=flagfile.read())

    # Get AES key
    with open('key', 'r') as key:
        AES_KEY = key.read()

    while True:
        connection, address = server_socket.accept()
        shares = SecretSharer.split_secret(AES_KEY, SEND_SHARDS, SHARDS)

        connection.send(CHALL_TEXT)
        for i in range(SEND_SHARDS):
            current_part = i + 1
            connection.send("Part {part_num}: {part}\n".format(part_num=current_part, part=shares[i]))

        connection.close()
