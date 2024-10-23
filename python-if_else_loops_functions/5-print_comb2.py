#!/usr/bin/python3
for numb in range(100):
    if numb < 99:
        print("{:02}, ".format(numb), end='')
    else:
        print("{:02}".format(numb))
