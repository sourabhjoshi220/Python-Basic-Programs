#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the oddNumbers function below.
def oddNumbers(l, r):

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        l = int(input().strip())

        r = int(input().strip())

        res = oddNumbers(l, r)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

        fptr.close()
