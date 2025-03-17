# # اینزرشن سورت
# # این کد بدون هیچ کمکی چه در نوشتن الگوریتم و چه در نوشتن کد، فقط توسط خودم انجام شده
# A = [int(x) for x in input().split()]
# answer = 0
# for i in range(1 , len(A)):
#     if A[i] < A[i - 1]:
#         for j in range(1 , i + 1):
#             if A[i] < A[i - j]:
#                 answer = i - j
#         A[answer : i + 1] = [A[i]] + A[answer : i]
# print(A)
#
# # بعد از نوشتن کد بالا و نظر خواستن از چند هوش مصنوعی، همشون این کد رو بعنوان کد بهتر برای اینزرشن سورت پیشنهاد دادن. خودمم دیدم بهتره
# A = [int(x) for x in input().split()]
# for i in range(1, len(A)):
#     key = A[i]
#     while (i - 1) >= 0 and A[i - 1] > key:
#         A[i] = A[i - 1]
#         i -= 1
#     A[i] = key
# print(A)

# بابل سورت
# این کد بدون هیچ کمکی چه در نوشتن الگوریتم و چه در نوشتن کد، فقط توسط خودم انجام شده
A = [int(x) for x in input().split()]
n = len(A)
i = 0
while i != n:
    i = 1
    for j in range(n - 1):
        if A[j] > A[j + 1]:
            A[j] , A[j + 1] = A[j + 1] , A[j]
        else:
            i += 1
print(A)

# بعد از نوشتن کد بالا و نظر خواستن از هوش مصنوعی، دیدم این کد بهتره
A = [int(x) for x in input().split()]
n = len(A)
swapped = True  # پرچم برای بررسی جابجایی

while swapped:
    swapped = False  # فرض میکنیم هیچ جابجایی رخ نداده
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            swapped = True  # اگر جابجایی رخ داد، پرچم را True میکنیم
    n -= 1  # بعد از هر تکرار، بزرگترین عنصر در جای درست است. نیازی به بررسی دوباره نیست.

print(A)