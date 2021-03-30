# Basic fermat primality test for prime numbers
#
# This will probably get integrated into a composite primality test.

import random

def primeTest(testNum):
  
  if (testNum % 2 == 0):
    return False
    
  upper_bound = testNum - 1
  witness = random.randrange(1, upper_bound, 1)
  
  # Do five iterations to weed out pseudoprimes
  isPrime = False
  i = 1
  while i < 5:
    if (witness ** (testNum - 1) % testNum == 1):
      isPrime = True
    else: isPrime = False
    
    witness = random.randrange(1, upper_bound, 1)
    i += 1
  
  return isPrime
