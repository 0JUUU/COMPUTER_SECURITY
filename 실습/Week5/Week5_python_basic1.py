"""
Python 기초

여러줄 주석
"""
# 한줄 주석

# 모듈을 import 하는 두가지 방법
import random
from pprint import pprint

def print_func(param1):
    pprint(param1)
    param2 = 1 + 2
    param2 += param1
    # + 뿐만 아니라 -, *, /, //(나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함, % 사용 가능

if __name__ == "__main__":
    val1 = 10
    val2 = 'apple'
    val3 = None
    
    rnd = random.randint(0, 9)

    # python에서 제공하는 built-in 자료구조
    print_func([val1, val2, val3, rnd])     # list type (c++ 의 vector와 유사)
    print_func((val1 + rnd, val2, val3))     # tuple type 
    print_func({val1, val2, val3, rnd})     # set type (순서가 없는 집합, c++의 set과 유사)
