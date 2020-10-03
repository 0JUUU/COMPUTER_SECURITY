"""
GCD(  a>=0, b>=0  )
"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a == b:
        return a
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(710, 310))