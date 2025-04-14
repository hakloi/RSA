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

def generate_keys():
    primes = sieve(10**5)
    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = choose_e(phi)
    d = modinv(e, phi)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    if message >= n:
        raise ValueError("Message too large for current key size")
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    try:
        msg = int(input("Input your secret code: "))
    except ValueError:
        print("ERROR: Input only integer, not float number.")
        exit(1)

    print("Original:", msg)

    if msg >= public_key[1]:
        raise ValueError("Message too large for current key size!")

    cipher = encrypt(msg, public_key)
    print("Encrypted:", cipher)

    decrypted = decrypt(cipher, private_key)
    print("Decrypted:", decrypted)
