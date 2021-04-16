
from composite_primality import composite_primality
from prime_generator import prime_gen
import random
import sys

digits = int(sys.argv[1]) - 1

#rand_num = random.randrange(10 ** digits,  (10 ** (digits + 1)) - 1, 1)
while True:
  #print(rand_num)
  rand_num = random.randrange(10 ** digits,  (10 ** (digits + 1)) - 1, 1)
  #rand_num = prime_gen(digits)
  if composite_primality(rand_num):
    print(rand_num, "is prime")
    break;