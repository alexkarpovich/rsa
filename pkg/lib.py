import random
from math import log
from typing import Optional


def is_miller_rabin_passed(n: int, k: Optional[int] = None) -> bool:
    """
    Miller-Rabin Primality Test tells us if n is a prime number with high probobility.

    :param int n: number to check
    :param int k: round count
    :return bool: is it probobly prime or exactly composite
    """

    round_count = k or int(log(n, 2))
    c = n - 1
    s = 1
    t = 0

    # From that formula n-1=2^s*t we need to find a pair max s
    # where s and t are both whole numbers
    while True:
        p = 2**s

        if c % p == 0:
            t = c // p
            s += 1
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

            elif x == c:
                continue

        return False

    return True




