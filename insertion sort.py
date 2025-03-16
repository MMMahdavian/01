A = [int(x) for x in input().split()]
for i in range(1, len(A)):
    key = A[i]
    while (i - 1) >= 0 and A[i - 1] > key:
        A[i] = A[i - 1]
        i -= 1
    A[i] = key
print(A)
print(A)
