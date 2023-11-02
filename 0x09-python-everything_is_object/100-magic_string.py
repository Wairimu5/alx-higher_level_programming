#!/usr/bin/python3

def magic_string():
    s = "BestSchool"
    return "".join([s * (i + 1) for i in range(len(s))])
