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

def random_prime_number(bits:int) -> int:
  while True:
    n = random.getrandbits(bits)
    n += 1 if n % 2 == 0 else 0

    if is_prime(n):
      return n

def mcm(x1:int, x2:int) -> int:
  if x1 == 0 or x2 == 0:
    return 0
  
  return abs(x1 * x2) // math.gcd(x1, x2)

def extended_mcd(a:int, b:int) -> tuple[int, int, int]:
  if b == 0:
    return (a, 1, 0)
  else:
    mcd, x1, y1 = extended_mcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (mcd, x, y)

def mod_inverse(e:int, lambda_n:int):
  mcd, x, _ = extended_mcd(e, lambda_n)
  if mcd != 1:
    raise ValueError("No existe el inverso multiplicativo modular de e y lambda(n) porque no son coprimos.")
  else:
    return x % lambda_n