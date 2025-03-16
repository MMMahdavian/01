# # # a = input()
# # # B = list(map(int, str(a)))
# # # print(B)
# # # C = set(B)
# # # print(C)
# # #
# # # a = input().split()
# # # L = list(map(int, a))
# # # print(L)
# # # #
# # # # a = []
# # # # a = a + map(int, input().split())
# # # # print(a)
# # # #
# # # # a = []
# # # # a += map(int, input().split())
# # # # print(a)
# # #
# # # a = [int(i) for i in input().split()]
# # # for i in range (len(a)):
# # #     a[i] += 1
# # #     print(a[i])
# #
# # # a = [int(i) for i in input().split()]
# # # b = int(input())
# # # if b == 1:
# # #     for i in range(len(a)):
# # #         if (i+1) % 2 == 0:
# # #             a[i] -= 3
# # #     print(a)
# # # elif b == 2:
# # #     for i in range(len(a)):
# # #         if (i+1) % 2 != 0:
# # #             a[i] *= a[i]
# # #     print(a)
# # # elif b == 3:
# # #     for i in range(len(a)-1):
# # #         if i == 0 or (i+1) % 4 == 1:
# # #             a[i] += a[i+1]
# # #     print(a)
# # # else:
# # #     print("یکی از اعداد 1 تا 3 را وارد کنید")
# #
# # n = int(input())
# # a = [0] * n
# # for i in range(n):
# #     a[i] = int(input())
# # print(a)
# # m = int(input())
# # # y = 0 # اگه قرار بود از حلقه for استفاده کنیم
# # # for i in range(n):
# # #     if a[i] == m:
# # #         print(i)
# # #         y = 1
# # # if y == 0:
# # #     print(m,"koja bood?")
# # i = 0
# # while i < n:
# #     if a[i] == m:
# #         print(i)
# #         break
# #     i += 1
# # if i == n:
# #     print(m, "koja bood?")
# #
# # # i = 1
# # # s = 0
# # # while i < 11:
# # #     s = s + i
# # #     i += 1
# # # print(s)
# #
# n = 1
# i = 0
# a = []
# while n != 0:
#     n = int(input())
#     a.append(n)
#     i += 1
# s = 0
# for i in range (len(a)):
#     s += a[i]
# print(s)

# a = int(input())
# jame_argham = a % 10
# while a > 1:
#     a //= 10
#     jame_argham += a % 10
# print(jame_argham)

# a = int(input())
# c = a
# B = []
# while c >=1:
#     B.append(c % 10)
#     c //= 10
# i = len(B)
# print(B, i)
# b = 0
# for j in range(i):
#     b += B[j] * 10 ** (i-j-1)
# print(b)
# if a == b:
#     print("*AYNEH*")
# else:
#     print("NORMAL")
# یک راه خیلی راحت تر برای حل سوال بالا:

# a = input()
# if str(a) == str(a)[::-1]:
#     print("*AYNEH*")
# else:
#     print("NORMAL")

# A = [int(i) for i in input().split()]
# B = [1]
# i = 0
# for j in range(1, len(A)):
#     if A[i] + 3 <= A[j]:
#         B.append(j + 1)
#         i = j
# for k in B:
#     print(k, end=" ")

"""با میزان مشخصی پول می خوایم بیشترین وزن کیک ممکن رو بخریم. وزن وقیمت هر کیک معلومه"""

"""داده ها:"""
# money = 89
# weight = [4, 6, 7, 7, 13, 9, 21]
# price = [35, 73, 70, 24, 59, 12, 15]
# """حل:"""
# n = len(weight)
# rate = [0] * n
# for i in range(n):
#     rate[i] = price[i] / weight[i]
# print(rate)
# for i in range(n):
#     for j in range(i):
#         if rate[i] < rate[j]:
#             rate[i], rate[j] = rate[j], rate[i]
#             price[i], price[j] = price[j], price[i]
#             weight[i], weight[j] = weight[j], weight[i]
# print("---")
# print(rate)
# print(weight)
# print(price)
# print("---")
# w = 0
# for i in range(n):
#     if money >= price[i]:
#         w = w + weight[i]
#         money = money - price[i]
#         print(f"weight{i}= {weight[i]}")
#         print(f"money{i}= {money}")
#     elif money > 0:
#         print("elsefase")
#         w = w + money / price[i] * weight[i]
#         print(f"weight{i}= {money / price[i] * weight[i]}")
#         print(f"money{i}= {money}")
#         money = 0
#         break
# print(f"weight total= {w}")

# a, b = 1 , 1000
# i = 0
# while b >= a:
#     n = (a + b) // 2
#     i = i + 1
#     print(f"q{i}. is {n} your number?")
#     x = input(f"input 's' , 'b' or 'e' if your number is smaller, bigger or equal to{n}:")
#     if x == "s":
#         b = n - 1
#     elif x == "b":
#         a = n + 1
#     elif x == "e":
#         print(f"***your nember was {n} and i win!***")
#         break
# print(f"total number of questions is {i}.")
"""
A = [[0] * 3 for i in range(3)]

def init_table(A):
    counter = 0
    for i in range(3):
        for j in range(3):
            counter += 1
            A[i][j] = counter

def print_table(A):
    for i in range(3):
        for j in range(3):
            print(A[i][j], end=" ")
        print()
    print()

init_table(A)
print_table(A)

for move in range(9):
    if move % 2 == 0:
        m = int(input("player 1:"))
        m -= 1
        if A[m // 3][m % 3] == "x" or A[m // 3][m % 3] == "o":
            print("Error! try again:")
            continue
        A[m // 3][m % 3] = "o"
        print_table(A)
        for i in range(3):
            if\
            (A[i][0] == "o" and A[i][1] == "o" and A[i][2] == "o") or\
            (A[0][i] == "o" and A[1][i] == "o" and A[2][i] == "o") or \
            (A[0][0] == "o" and A[1][1] == "o" and A[2][2] == "o") or \
            (A[0][2] == "o" and A[1][1] == "o" and A[2][0] == "o"):
                print("***player1 win!***")
                break
    else:
        m = int(input("player 2:"))
        m -= 1
        if A[m // 3][m % 3] == "x" or A[m // 3][m % 3] == "o":
            print("Error! try again:")
            continue
        A[m // 3][m % 3] = "x"
        print_table(A)
        for i in range(3):
            if\
            (A[i][0] == "x" and A[i][1] == "x" and A[i][2] == "x") or\
            (A[0][i] == "x" and A[1][i] == "x" and A[2][i] == "x") or \
            (A[0][0] == "x" and A[1][1] == "x" and A[2][2] == "x") or \
            (A[0][2] == "x" and A[1][1] == "x" and A[2][0] == "x"):
                print("***player2 win!***")
                break

print("The End!")
"""


# while True:
#     x = int(input())
#     if x != 1 and x != 2:
#         print("just enter 1 or 2:", end=" ")
#     else:
#         break
# print("the end")

a = False
b = True
c = (a or b) and not(a and b)
print(c)
a = bool(input())
print(a)

# b = 2.9
# a = b < 3
# print(a)

تعریف تمام ترکیب‌های ممکن برای A, B, C
from itertools import product


def check_distributive_law():
    # ایجاد جدول حقیقت: تمامی ترکیب‌های ممکن از True و False برای A, B, C
    truth_table = list(product([True, False], repeat=3))

    is_valid = True  # فرض می‌کنیم قانون درست است

    for A, B, C in truth_table:
        # محاسبه دو طرف اتحاد منطقی
        left_side = A and (B or C)
        right_side = (A and B) or (A and C)

        # مقایسه نتایج
        if left_side != right_side:
            print(f"قانون نقض شد برای A={A}, B={B}, C={C}")
            is_valid = False
            break

    if is_valid:
        print("این اتحاد منطقی همیشه برقرار است!")
    else:
        print("این اتحاد منطقی برقرار نیست!")


# اجرای برنامه
check_distributive_law()


# from itertools import product

# # تولید تمام ترکیب‌های ممکن
# truth_table = list(product([1, 2, 3], repeat=3))
# print(truth_table)
# print(len(truth_table))
