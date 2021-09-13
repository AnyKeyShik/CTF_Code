#! /usr/bin/env python3

import base65536
import pybase100 as base100
import base64

with open('flag', 'r') as flag_file:
    flag = flag_file.read()
    print(flag, end='\n')
    flag = flag.encode('utf-8')

# Base64
flag = base64.b64encode(flag)
print(flag.decode('utf-8'), end='\n\n')

# Base100
flag = base100.encode(flag)
print(flag.decode('utf-8'), end='\n\n')

# Base65536
flag = base65536.encode(flag)
print(flag, end='\n\n')

with open('flag.enc', 'w') as flag_file:
    flag_file.write(flag)
    print("Encrypted successful!")
