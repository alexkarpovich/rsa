import random
from math import log, gcd
from typing import Optional


def is_miller_rabin_passed(n: int, k: Optional[int] = None) -> bool:
    """
    Miller-Rabin Primality Test tells us if n is a prime number with high probobility.

    :param int n: number to check
    :param int k: round count
    :return bool: is it probobly prime or exactly composite
    """

    # Even numbers cannot be primes
    if n != 2 and n % 2 == 0:
        return False
    
    round_count = k or int(log(n, 2))
    c = n - 1
    s = 1
    t = 0

    # From that formula n-1=2^s*t we need to find a pair max s
    # where s and t are both whole numbers
    while True:
        p = 2**s

        if c % p == 0:
            t_condidate = c // p
            s += 1

            if t_condidate % 2 == 0:
                continue

            t = t_condidate
        else:
            break

    
    for i in range(round_count):
        a = random.randint(2, n - 2)
        # x = a^t mod n
        x = pow(a, t, n)

        if x == 1 or x == c:
            continue
        
        for j in range(s - 1):
            # x = x^2 mod n
            x = pow(x, 2, n)

            if x == 1:
                return False

            if x == c:
                break
        else:
            return False

    return True


def get_random_num(length: int = 1024, odd_only: bool = False) -> int:
    """
    Generates random number with specified length
    :param int length: digits count
    :param bool odd_only: to get only odd numbers

    :return int: random number
    """

    rand_num = random.randint(10**(length-1), 10**length - 1)

    if odd_only:
        rand_num |= (1 << length - 1) | 1

    return rand_num


def get_random_prime(length: int = 1024) -> int:
    '''Generates random prime number with specified length'''

    while True:
        rand_odd = get_random_num(length, True)

        if is_miller_rabin_passed(rand_odd):
            return rand_odd


def xgcd(a: int, b: int):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1

    return b, x0, y0

def gen_rsa(length: int = 2048):
    half_length = length // 2

    # Step 1: Generating 2 prime numbers p, q
    p = get_random_prime(half_length)
    print(f'p = {p}')

    q = get_random_prime(half_length)
    print(f'q = {q}')

    n = p * q
    phi = (p - 1) * (q - 1)
    print(f'n = {n}\nphi = {phi}')

    # Step 2: Searching for e that is relativly prime to (p - 1) * (q - 1)
    while True:
        e = get_random_num(half_length)
        
        if gcd(e, phi) == 1:
            break

    print(f'e = {e}')

    # Step 3: Calculating d, the mod inverse of e
    *_, d = xgcd(phi, e)

    print(f'd = {d}')
    
    return (d, n), (e, n)


def encrypt(message: str, key: tuple) -> str:
    e, n = key
    cipher = [pow(ord(char), e, n) for char in message]

    return cipher


def decrypt(cipher: str, key: tuple) -> str:
    d, n = key
    message = [chr(pow(char, d, n)) for char in cipher]

    return ''.join(message)