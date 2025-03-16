def min(A):
    m = A[0]
    for i in range (1, len(A)):
        if A[i] < m:
            m = A[i]
    return m
def max(A):
    m = A[0]
    for i in range (1, len(A)):
        if A[i] > m:
            m = A[i]
    return m

A = [int(j) for j in input().split()]
B = [3070, 633, 3040, 2008, 90.1, 1690]
print(min(B), max(B), min(A), max(A))