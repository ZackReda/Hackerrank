# Link : https://www.hackerrank.com/challenges/apple-and-orange/problem
# Name : Apple and Orange
# Level : Easy
# Max Score : 10

''''''''''''''''''''''''''''''''''''

#!/bin/python

import sys


    # Complete this function

if __name__ == "__main__":
    s, t = raw_input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = raw_input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = raw_input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = map(int, raw_input().strip().split(' '))
    orange = map(int, raw_input().strip().split(' '))
    print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))
