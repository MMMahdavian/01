
# سورت اعداد داده شده به دو روش که منظق هردو یکی است

# روش اول
def sort(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]
    return A
L = [int(i) for i in input().split()]
print(sort(L))

# روش دوم
def sort(A):
    n = len(A)
    for i in range(n):
        m = A[i]
        p = i
        for j in range(i+1, n):
            if A[j] < m:
                m = A[j]
                p = j
        A[p] = A[i]
        A[i] = m
    return A
L = [int(i) for i in input().split()]
print(sort(L))

def myMove(n, A):
    if A % 4 == 0:
        while n < A:
            x = int(input("bebras:"))
            n += x
            print(f"so n= {n}")
            if n == A:
                result = "bebras won! horaaaa!"
                break
            x = (A - n) % 4
            print(f"i enter: {x}")
            n += x
            print(f"so n= {n}")
            if n == A:
                result = "i won! horaaaa!"
                break
    else:
        while n < A:
            x = (A - n) % 4
            print(f"i enter: {x}")
            n += x
            print(f"so n= {n}")
            if n == A:
                result = "i won! horaaaa!"
                break
            x = int(input("bebras:"))
            n += x
            print(f"so n= {n}")
            if n == A:
                result = "bebras won! horaaaa!"
                break
    return result
A = int(input("neter a digit: "))
n = 0
print(myMove(n, A))