
import random

def rabin_miller_primality(randPrime):
  # This primality test is proven to always register primes below 10^16, with strong probability that it will past that.
  #print("Rabin Miller primality testing")
  if randPrime % 2 != 0 and randPrime < 10 ** 16 or randPrime == 2:
    # Calculate the powers of 2 in the prime number
    s = randPrime - 1
    exponent = 0      
    while s % 2 == 0: 
      s //= 2
      exponent += 1
    
    # check 40 times 
    for i in range(40):
      point_a = random.randrange(1, randPrime - 1, 1)
      
      checkNum = pow(point_a, s, randPrime)
      if checkNum != 1:
        j = 0
        while checkNum != randPrime - 1:
          if j == exponent - 1:
            return False
          else:
            j = j + 1
            checkNum = pow(checkNum, 2, randPrime)
            
      #print(True)
      return True
          
  else:
    #print(False)
    return False
  
  