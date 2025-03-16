# def search(key, my_list, eggs):
#     turn = 0
#     while eggs > 0:
#         floor = my_list[3 * turn + 1]
#         turn += 1
#         if floor >= key:
#             eggs -= 1
#             if floor == key:
#                 return turn
#             elif floor - 1 == key:
#                 turn += 1
#                 eggs -= 1
#                 return turn
#             else:
#                 turn += 1
#                 eggs -= 1
#                 return turn
#
# my_list = [i for i in range(101)]
# key = 79
# eggs = 3
# print(search(key, my_list, eggs))

def search(key, my_list, eggs):
    turn = 1
    floor = my_list[1]
    while floor < key:
        turn += 1
        floor += 3
        if floor >= key:
            eggs -= 1
            if floor == key:
                return turn
            if floor - 1 == key:
                turn += 1
                eggs -= 1
                return turn
            if floor - 2 == key:
                turn += 1
                eggs -= 1
                return turn
    return turn
my_list = [i for i in range(101)]
key = 79
eggs = 3
print(search(key, my_list, eggs))