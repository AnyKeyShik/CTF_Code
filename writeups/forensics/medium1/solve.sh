#!/bin/sh

for i in {1..660}
do
    fatcat dump -L $i 2>/dev/null | grep '^f' >> files
done
