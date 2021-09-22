#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

#################### FIRST KEY ####################
key = rsa.generate_private_key(backend=default_backend(), public_exponent=3, key_size=2048)

key_pub = key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
key_priv = key.private_bytes(encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption())

with open('bob', 'wb') as bob:
    bob.write(key_priv)

with open('bob.pub', 'wb') as bobpub:
    bobpub.write(key_pub)


################### SECOND KEY #######################
key = rsa.generate_private_key(backend=default_backend(), public_exponent=3, key_size=2048)

key_pub = key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
key_priv = key.private_bytes(encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption())

with open('alice', 'wb') as alice:
    alice.write(key_priv)

with open('alice.pub', 'wb') as alicepub:
    alicepub.write(key_pub)


#################### THIRD KEY ###########################
key = rsa.generate_private_key(backend=default_backend(), public_exponent=3, key_size=2048)

key_pub = key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
key_priv = key.private_bytes(encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption())

with open('eve', 'wb') as eve:
    eve.write(key_priv)

with open('eve.pub', 'wb') as evepub:
    evepub.write(key_pub)

