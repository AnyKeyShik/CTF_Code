#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    REAL_FLAG = "oren_ctf_spectre!"
    FAKE_FLAG = "oren_ctf_z3r0d4y!"

    license = [chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(REAL_FLAG, FAKE_FLAG)]

    with open('license.bin', 'wb') as licensefile:
        for byte in license:
            licensefile.write(bytes(byte, 'utf-8'))


if __name__ == "__main__":
    main()
