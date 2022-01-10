# 두 배열의 원소 교체

'''
두 배열은 N개의 자연수로 이루어져 있다.
최대 K번의 바꿔치기 연산을 수행하는 데, 바꿔치기 연산은
배열 A의 원소와 배열 B의 원소를 서로 바꾸는 것을 말한다.
최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 
'''

N, K = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

A = quick_sort(A)
B = quick_sort(B)

for i in range(K):
    if A[i]<B[N-1-i]:
        A[i],B[N-1-i] = B[N-1-i], A[i]
    else:
        break
print(sum(A))

'''
두 배열의 원소가 최대 100,000개까지 입력되기 때문에, 최악의 경우 O(NlogN)을 사용
'''
