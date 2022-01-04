"""
스택 자료구조는 리스트로 구현할 수 있음

삽입: append, 삭제: pop
"""

s=[]
s.append(1)
s.append(2)
print(s.pop())


from collections import deque
"""
큐 자료구조 deque

삽입: append, 삭제: popleft

리스트 자료구조를 사용하면 시간 복잡도에서 손해 봄

뒤집고 싶으면 queue.reverse() 
"""
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())
