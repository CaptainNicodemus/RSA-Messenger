
import random
import math

def prime_gen():

  # Pick a random integer in a large range of integers
  rand_num = random.randrange(1000, 25 * 10 ** 9, 1)
  
  # no evens
  while rand_num % 2 == 0:
    rand_num = random.randrange(1000, 25 * 10 ** 9, 1)
   
  check_num = rand_num - 1
  
  s = 0
  while math.floor(check_num / s ** 2) % 2 == 0:
    s += 1
    
  d = check_num / s ** 2
  
  a = random.randrange(1, rand_num - 1, 1)
  
  if a ** d % rand_num != 1:
    r = random.randrange(0, s, 1)
    
    if 2 ** ((d ** a) ** r) % rand_num == check_num:
      return rand_num
    else:
      return 0
    