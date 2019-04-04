#########################
# !!! SOLUTION CODE !!! #
#########################


#!/bin/python3

import math
import os
import random
import re
import sys

def con_ones(n):
  """Calculate the max number of consecutive 1's from binary."""
  result, count = 0, 0
  consecutive = []
  for i in [int(j) for j in f'{n:b}']:
    if i:
      count = count + 1
      if count > 0:
        result = result + 1
    else:
      consecutive.append(result)
      result, count = 0, 0
    
  consecutive.append(result)  
  return max(consecutive)


if __name__ == '__main__':
    n = int(input())
    print(con_ones(n))
