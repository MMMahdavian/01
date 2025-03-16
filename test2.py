# a = 7
# b = 4
# print("a is: %i b is: %i" %(a,b))

# name = "Sara"
# age = 30
# height = 1.65
#
# print(name+"is"+str(age))
#
# print(type(name))
# print(type(age))
# print(type(height))

# x = 1.6543
# y=7
# print("Height: %.2f meters %i" %(x,y))

# value = 1234.5678
# formatted_value = f"{value:.2f}"  # خروجی: 1234.57

# mfl = [11,12,13,15,17,19,20]
# mfr = range (11,20)
#
# print (str(mfr)+ " "+"and list"+str(mfl))

# x = "NjduJ"
# y = "bOOk"
# print (y.upper())

# s = input('input a sentence or phrace: ')
# x = input (f"input favourite characters of '{s}': ")
# print(s.count(x))

# L = input('input a sentence or phrace: '). split()
# print(L[-1])

# s = input("input a sentence or phrace: ")
# s = s.rstrip()
# i = s.rfind(" ")
# print (s[i+1:])

# p = input () ; print (p)
# x = "Hello, World!"
# print(x[0:5] + x[7:11])

# x = "Hello, world"
# x = x.replace("w", "r")  # Output: Hello, universe
# print(x)

help (str.replace)

# original_string = "سلامتا ایتایتایتاییاتایاثاغساساااساساسااسااساسا دنیا و دنیا"
# new_string = original_string.replace("ا", "ت", -1)  # تنها اولین مورد را تغییر می‌دهد
# print(new_string)  # خروجی: "سلام جهان و دنیا"

# x = "Hello, World!"
# reversed_x = x[::-1]
# print(reversed_x) # خروجی: !dlroW ,olleH

# print("Hello\nWorld")

# favorite_fruits = ['anjir' , 'anar' , 'hensevane' , 'moz', 'golabi']
# print(favorite_fruits[3])

# my_info = {'my_name' : 'mahdi' , 'my_age' : 38 , 'my_city' : 'mashad'}
# print (my_info)

# x = 6
# p = x > 0 and x > 6
# print(p)

# x = 6
# print(x > 0 and x > 6)

# a = input ("a = ")
# b = input ("b = ")
#
# if a < b :
#     print('a is less than b')
# elif a > b :
#     print('a is greater than b')
# else :
#     print('a is equal to b')

# height = float(input("Enter your height: "))
# print("Your height is:" , height)

# چاپ اعداد 1 تا 5
# for i in range(1, 6):
#     print(i)


# چاپ اعداد از 1 تا 5 با حلقه while
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # افزایش مقدار i در هر تکرار

#
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue  # اگر i زوج باشد، از بقیه تکرار رد می‌شود
#     print(i)


# for i in range(1, 5):
#     if i % 2 == 0:
#         print(f"{i} is even")  # این دستور داخل شرط و حلقه است
#     print("Inside the loop")  # این دستور فقط داخل حلقه است و نه داخل شرط
#
# print("Outside the loop")  # این دستور خارج از حلقه است

# for a in range (1 , 11):
#     if a >= 7:
#         break
#     print (a)


# for a in range (1, 11):
#     if a % 2 != 0:
#         print (a)

# def greet():
#     print("Hello!")

# def add(a, b):
#     return a + b
# print (add ( 4,76 ))

# def square(a):
#     return a**2
# print (square(3))

# def is_even (a):
#     if a % 2 == 0:
#         return ('true')
#     else:
#         return ('false')
# a=int(input('input a digit :'))
# print(is_even(a))

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(598))


# class car:
#     def __init__(self, brand, model):
#         self.brnd= brand
#         self.mdl= model
#     def start(self):
#         print (self.brnd+' '+ self.mdl+ ' '+ 'is starting')
#
# car1= car('benz', 's500')
#
# print(car1.start())

class BankaAccount:
    def __init__(self, owener, balance=0):
        self.owener= str(owener)
        self.balance= float(balance)
    def deposit(self, amount):
        self.balance= self.balance+ amount
    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance= self.balance- amount
        else:
            print('not efficient balance')
    def get_balance(self):
        return self.balance

mahdiBA= BankAccount('mahdi', 104)

mahdiBA.deposit(16)
print(mahdiBA.get_balance())

mahdiBA.withdraw(65)
print(mahdiBA.get_balance())

mahdiBA.withdraw(58)
print(mahdiBA.get_balance())

class SavingsAccount(BankAccont):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super.__init__(owener, balance)
        self.interest_rate= float(interest_rate)
    def ci(self):
        interest= self.interest_rate* self.balance
        return interest
savings= SavingAccount(mahdi, 1000, 0.2)
savings.deposit(500)
savings.ci()
print(savings.get_balance())






# class mahdavian:
#     def __init__(self, gender, name, age, weight, height):
#         self.gender= gender
#         self.name= name
#         self.age= int(age)
#         self.weight= float(weight)
#         self.height= float(height)
#     def h(self):
#         if self.gender== 'man':
#             self.height= self.weight+ 100
#         else:
#             self.height= self.weight+ 105
#         return self.height
# gender= input()
# name= input()
# age= int(input())
# weight= float(input())
# height= float(input())
# somemhdvn= mahdavian(gender, name, age, weight, height)
# print(somemhdvn.h())

