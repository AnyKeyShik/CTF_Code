from urllib.request import urlopen, Request
import sys


def get_next_message(hash_str, const):
    new_request = Request(
        url="http://{}/".format(sys.argv[1]) + hash_str,
        headers={'User-Agent': "snake3.smth + {}".format(const)}
    )
    print(hash_str)
    return urlopen(new_request).msg


i = 0
global_hash_string = get_next_message("", i)
while "oren_ctf" not in global_hash_string:
    i += 1
    print(i, global_hash_string)
    global_hash_string = get_next_message(global_hash_string.split()[-1], i)
print(global_hash_string)
