"""
miller-rabin prime test

Test if n is prime with error probability less than 2^(−𝑠).

"""

import random
from exponentiation import exp

Prime = 0
Composite = 1


def miller_rabin(n, s):
    if n == 2:
        return Prime
    elif n % 2 == 0:
        return Composite

    for _ in range(s):
        a = random.randint(1, n-1)
        if test(a, n) == True:
            return Composite

    return Prime

def test(a, n):
    
    # t,u --> t >=1, u : odd & n-1 = 2^t * u
    c = 0
    t = n-1
    while t % 2 == 0 :
        c += 1
        t = t/2
    t = c
    u = (n-1) // (2 ** t)
    
    # x0 = a^u mod n --> modular exponentiation
    x0 = exp(a, u, n)

    # for문
    for _ in range(t):
        x1 = (x0**2) % n
        if x1 == 1:
            if x0 != 1:
                if x0 != n-1:
                    return True         # NSR test
        x0 = x1
        x1 = 0

    # Fermat test
    if x0 != 1 :
        return True

    return False


if __name__ == "__main__":

    primes = [7879, 7883, 7901, 7907, 7919, 7927, 7933, 7937, 7949, 7951,
              7963, 7993, 8009, 8011, 8017, 8039, 8053, 8059, 8069, 8081,
              8087, 8089, 8093, 8101, 8111, 8117, 8123, 8147, 8161, 8167]

    for p in primes:
        result = miller_rabin(p, 20)
        if result == Prime:
            print("Prime")
        elif result == Composite:
            print("Composite")
        else:
            print("Undefined")
