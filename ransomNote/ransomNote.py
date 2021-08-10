#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # make a dict of each
    mag = {}
    for word in magazine:
        if word in mag:
            mag[word] += 1
        else:
            mag[word] = 1
    n= {}
    for word in note:
        if word not in mag:
            print('No')
            return
        if word in n:
            if n[word] == mag[word]:
                print('No')
                return
            n[word] += 1
        else:
            n[word] = 1
    print('Yes')
    return



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
