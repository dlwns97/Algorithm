"""
재귀함수 예제

반복문을 사용할 때 보다 코드가 더 간결하고 직관적
"""

# Factorial
def factorial(n):
    return 1 if n == 1 else n*factorial(n-1)
print(factorial(3))

# 유클리드 호제법
"""
두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 하면
A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
"""
def gcd(a,b):
    return b if a%b==0 else gcd(b, a%b)
print(gcd(192,162))
