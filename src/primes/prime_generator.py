
import random

def prime_gen(digits):
  
  while True:
    # Pick a random integer in a large range of integers
    rand_num = random.randrange(10 ** digits,  (10 ** (digits + 1)) - 1, 1) # This can be updated to be more robust
    #print(rand_num)
    # no evens
    while rand_num % 2 == 0:
      rand_num = random.randrange(10 ** digits,  (10 ** (digits + 1)) - 1, 1)
      #print(rand_num)
     
    check_num = rand_num - 1
    
    s = 1
    while True:
      if int(check_num / s ** 2) % 2 == 0:
        break
      s += 1
      
    d = int(check_num / s ** 2)
    
    a = random.randrange(1, rand_num - 1, 1)
    
    #print("S: ", s)
    #print("D: ", d)
    #print("A: ", a)
    
    if int(a ** d % rand_num) != 1:
      r = random.randrange(0, s, 1)
      
      if int(2 ** ((d ** a) ** r)) % rand_num == check_num:
        return rand_num
    