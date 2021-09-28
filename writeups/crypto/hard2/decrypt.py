#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cryptor


def decrypt(cipher, crypted):
    return cipher.decrypt(crypted)


def main():
    server_msgs = [
        "0RIGdbNapocC9vboA6JibpPFofBO111RQA10aSzSg5zxEjA8K2QFJpBDZTWOWQ==",
        "jxJ263lpDOs1iu8PsFHFrYjNxc7LwKeXuSwlx2/Sjw==",
        "ugI=",
        "uVf4eg==",
        "b6dQ3YQ0RWHPNE0Z7eRKNDlLCMoF59iJM/cwxaMyADGfxYjHqrQenQ==",
        "SrmN"
    ]
    client_msgs = [
        "cDxuXhw=",
        "gdOXQjD8ruH6VRtj0topdqS3SAUKy+1nee2XFCpZA/s=",
        "uAVKR1ir",
        "njdw"
    ]

    priv_x = 263085750118593959
    priv_y = 99484538495976508

    client_cipher = cryptor.cryptor(priv_x, priv_y, "client")
    server_cipher = cryptor.cryptor(priv_x, priv_y, "server")

    print(decrypt(client_cipher, server_msgs[0]))
    print(decrypt(client_cipher, server_msgs[1]))
    for i in range(4):
        print(decrypt(server_cipher, client_msgs[i]))
        print(decrypt(client_cipher, server_msgs[i + 2]))


if __name__ == "__main__":
    main()
