import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input()) 
    mul=1
    for a in range(1,11):
        mul = n*a
        print(n,'x',a,'=',mul)
