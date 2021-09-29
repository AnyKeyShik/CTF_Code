#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

if subprocess.Popen(['./problem']).wait() != 0:
    print("Wow, you\'ve crushed this")

    flagfile = open('flag')
    if not flagfile:
        print("Flag is missing, tell admin")
    else:
        print(flagfile.read())
