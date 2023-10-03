#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if chr(a) not in 'qe':
        print("{:c}".format(a), end='')
