#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


def gen_key():
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=3, key_size=2048)

    key_pub = key.public_key().public_bytes(serialization.Encoding.PEM,
                                            serialization.PublicFormat.SubjectPublicKeyInfo)
    key_priv = key.private_bytes(encoding=serialization.Encoding.PEM,
                                 format=serialization.PrivateFormat.TraditionalOpenSSL,
                                 encryption_algorithm=serialization.NoEncryption())

    return key_pub, key_priv


def main():
    alice_pub, alice_priv = gen_key()
    bob_pub, bob_priv = gen_key()
    eve_pub, eve_priv = gen_key()

    with open("alice", 'wb') as alice, open("alice.pub", 'wb') as alicepub:
        alice.write(alice_priv)
        alicepub.write(alice_pub)

    with open("bob", 'wb') as bob, open("bob.pub", 'wb') as bobpub:
        bob.write(bob_priv)
        bobpub.write(bob_pub)

    with open("eve", 'wb') as eve, open("eve.pub", 'wb') as evepub:
        eve.write(eve_priv)
        evepub.write(eve_pub)


if __main__ == '__main__':
    main()
