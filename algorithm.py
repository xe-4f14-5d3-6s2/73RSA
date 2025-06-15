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

def random_prime_number() -> int:
  while True:
    n = random.randint(16, 2047)
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


def text_to_number(text:str):
  n = [ord(c) for c in text]
  return n

def number_to_text(ns: list[int]):
  c = [chr(n) for n in ns]
  return ''.join(c)


def generate_keys():
  p = random_prime_number()
  q = random_prime_number()

  n = p * q

  e = 65537

  lambda_n = mcm(p-1, q-1)

  d = mod_inverse(e, lambda_n)

  return (e, d, n)

def encrypt(message: str, key: int, n: int):
  c = [f"{(m ** key) % n}" for m in text_to_number(message)]

  return ".".join(c)

def decrypt(digest: str, key: int, n: int):
  message = number_to_text(
    [(int(c)**key) % n for c in digest.split(".")]
  )

  return message