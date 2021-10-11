#!/usr/bin/env python3
# -*- coding: utf-8 -*-

keyboardMap = {
    2: "PostFail",
    4: "a",
    5: "b",
    6: "c",
    7: "d",
    8: "e",
    9: "f",
    10: "g",
    11: "h",
    12: "i",
    13: "j",
    14: "k",
    15: "l",
    16: "m",
    17: "n",
    18: "o",
    19: "p",
    20: "q",
    21: "r",
    22: "s",
    23: "t",
    24: "u",
    25: "v",
    26: "w",
    27: "x",
    28: "y",
    29: "z",
    30: "1",
    31: "2",
    32: "3",
    33: "4",
    34: "5",
    35: "6",
    36: "7",
    37: "8",
    38: "9",
    39: "0",
    40: "Enter",
    44: "Space",
    45: "-",
    47: "[",
    48: "]",
    57: "CapsLock"
}

with open('hexoutput', 'r') as keys:
    for line in keys:
        bytesArray = bytearray.fromhex(line.strip())

        for byte in bytesArray:
            if byte != 0:
                value = int(byte)

                if value in keyboardMap:
                    print(keyboardMap[value])
                else:
                    print("Unknown key {:d}!".format(value))
