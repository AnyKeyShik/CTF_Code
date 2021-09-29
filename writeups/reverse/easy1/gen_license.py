#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    xored = ['\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x09', '\x15', '\x17', '\x0c', '\x10', '\x13', '\x1c', '\x00']

    with open('license.bin', 'wb') as licensefile:
        for xb in xored:
            licensefile.write(bytes(xb, 'utf-8'))


if __name__ == "__main__":
    main()
