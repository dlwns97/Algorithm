import sys

k = int(sys.stdin.readline().rstrip())
stack=[]
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    stack.append(num) if num!=0 else stack.pop()
print(sum(stack))

"""
sys.stdin.readline()와 input의 차이점

둘은 같은 역할을 하지 않는데

input() 내장 함수는 parameter로 prompt message를 받을 수 있다.
sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다.
sys.stdin.readline()은 직접 .rstrip()을 하지 않으면 개행문자를 포함하여 리턴한다

따라서 input() 내장 함수는 sys.stdin.readline()과 비교해서 속도가 느리다.
"""

