A = [int(x) for x in input().split()]
answer = 0
for i in range(1 , len(A)):
    if A[i] < A[i - 1]:
        for j in range(1 , i + 1):
            if A[i] < A[i - j]:
                answer = i - j
        A[answer : i + 1] = [A[i]] + A[answer : i]
print(A)