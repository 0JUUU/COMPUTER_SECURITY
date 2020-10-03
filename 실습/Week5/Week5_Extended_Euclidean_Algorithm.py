"""
Extended Euclidean Algorithm (Iterative version)  ( a >= b )  # 재귀함수로도 구현 가능

return (x, y, r) such that a * x + b * y = r = gcd(a, b)
loop invariant (루프 중에 유지하는 툴):
a * x_1 + b * y_1 = r_1
a * x_2 + b * y_2 = r_2

"""

def extended_euclid(a, b):

    # case trivial --> 직접 처리하도록
    if a == b:  
        return 1, 0, a    
    elif b == 0:
        return 1, 0, a

    # 그렇지 않으면 초기화    
    else:
        x_1 = 1
        y_1 = 0
        r_1 = a

        x_2 = 0
        y_2 = 1
        r_2 = b

        while r_2 != 0:
            q = r_1 // r_2

            r_t = r_1 - q * r_2
            x_t = x_1 - q * x_2
            y_t = y_1 - q * y_2

            x_1, y_1, r_1 = x_2, y_2, r_2
            x_2, y_2, r_2 = x_t, y_t, r_t
        
        return x_1, y_1, r_1

"""
Multiplicative Inverse (모듈러 연산 곱의 역원)

x = a^-1 mod n
a * x mod n = 1
"""

def m_inv(a, n):
    x, y, r = extended_euclid(n, a % n)
    if r != 1:
        print("No multiplicative inverse")
        return
    else:
        return y % n

if __name__ == "__main__":
    print(extended_euclid(710, 310))
    print(m_inv(710, 310))