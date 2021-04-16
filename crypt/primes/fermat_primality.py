# Basic fermat primality test for prime numbers
#
# This will probably get integrated into a composite primality test.

import random

def fermat_primality(randPrime):
  
  #print("Fermat primality testing...")
  if (randPrime % 2 == 0 or randPrime < 3 or randPrime % 5 == 0):
    return False
    
  upper_bound = randPrime - 1
  witness = random.randrange(1, upper_bound, 1)
  
  # Do five iterations to weed out pseudoprimes
  isPrime = False
  
  for i in range(0, 5):
    #print(i)
    if (witness ** (randPrime - 1) % randPrime == 1):
      isPrime = True
    else: 
      isPrime = False
      break
    witness = random.randrange(1, upper_bound, 1)
  
  return isPrime
