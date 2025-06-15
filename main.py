import math, random, numpy as np

def is_prime(number:int) -> bool:
  if number % 2 == 0 or number <= 1:
    return False
  if number == 2:
    return True
  
  limit = int(np.sqrt(number)) + 1

  pos = np.arange(3, limit, 2)

  for i in pos:
    if number % i == 0:
      return False
  return True