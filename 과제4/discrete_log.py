"""
Discrete logarithm

a: given number
b: base
m: modulus

log_{b,m}(a)

"""

# from tqdm import tqdm  # progress bar
from exponentiation import exp


def dlog(b, a, m):
    for i in range (1, m) :
        x = exp(b,i,m) % m
        if x == a:
            return i
    return None


if __name__ == "__main__":
    base = 2
    modulus = 65537  # 2 ** 16 + 1

    expos = [
        1,
        2,
        65535
    ]

    try:
        # for expo in tqdm(expos):
        for expo in expos:
            powed = exp(base, expo, modulus)
            loged = dlog(base, powed, modulus)
            print("({},{},{},{},{}),".format(expo, base, powed, loged, modulus))
            assert expo == loged
        print(">> All the tests passed <<")
    except:
        print("expo({}) and loged({}) is not equal".format(expo, loged))
