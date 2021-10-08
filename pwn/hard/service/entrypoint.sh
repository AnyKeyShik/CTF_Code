#!/bin/sh

nsjail \
    --mode l \
    --port 31337 \
    --time_limit 30 \
    --disable_proc \
    --bindmount_ro /bin/ \
    --bindmount_ro /var/service/ \
    --cwd /var/service/ \
    --hostname shop \
	--max_cpus 1 \
    -- \
    ./shop
