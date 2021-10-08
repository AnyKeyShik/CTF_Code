#!/bin/bash

INPUT="message.wav"
OUTPUT="result.txt"

for k in $(seq 256 256 4096); do
    echo "k = $k"
    python2 "py_stego_phase/stego_phase.py" -i $INPUT -m $OUTPUT -k $k && \
    cat $OUTPUT | grep -a "oren" && rm result.txt && break
done
