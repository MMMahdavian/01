# x= int(input())
# f= 0
# for i in range(x+1):
#     f= f+i
#     print("f=", f)
# print(f) #مجموع اعداد یک تا ایکس

# n = int(input("Enter a number: ")) #بهترین کد واسه فاکتور یل
# a = 1
# for i in range(2, n + 1):
#     a *= i
# print(n, "! =", a)


# n = int(input())
# print(n*"*")
# for i in range(n-2):
#     print("*" + (n-2)*" " + "*")
# if n>1:
#     print(n*"*")

# n = int(input())  # تعداد اعداد را از کاربر می‌گیریم
# numbers = [] # لیست خالی برای ذخیره اعداد
# print(f"{n} adad ra be tartib vard konid:")
# for i in range(n): # گرفتن اعداد به کمک حلقه
#     value = int(input(f"adade {i+1}: "))
#     numbers.append(value)
#
# print(numbers)


A = [int(i) for i in input().split()]
n = len(A)
for i in range (n):
    for j in range (i + 1, n):
        if A[j] < A[i]:
            A[j], A[i] = A[i], A[j]
        print(i ,j, A)
print(A)