import random
import math


def sieve(limit):
    # создаем список флагов, где индекс - число, а значение T показатель простого числа
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num] == True:
            for mult in range(num * num, limit + 1, num): 
                # начиная с квадрата этого числа все кратные числа num - непростые
                is_prime[mult] = False
                
    return [num for num, prime in enumerate(is_prime) if prime]


def choose_e(phi):
    e = random.randrange(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    return e


def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0


primes = sieve(10 ** 6) # по условию
p = random.choice(primes)
q = random.choice(primes)
# print(p, q, len(primes))

if p == q:
    q = random.choice(primes)
    
# расчёт n и функции Эйлера φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# выбор открытой экспоненты e
e = choose_e(phi)

# вычисление закрытой экспоненты d
d = modinv(e, phi)

# создание ключей:
public_key = (e, n)
private_key = (d, n)

# шифрование, дешифрование
def encrypt(message, pubkey):
    e, n = pubkey
    return pow(message, e, n)  # (m ** e) % n

def decrypt(cipher, privkey):
    d, n = privkey
    return pow(cipher, d, n)  # (c ** d) % n

