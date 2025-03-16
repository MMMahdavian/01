def search(key, my_list, eggs):
    for turn in range((len(my_list) + 2) // 3):
        print("**********")
        print(f"turn+1= {turn+1}= tedade partabha")
        index = 3 * turn + 1
        print(f"index= {index}")
        if index >= len(my_list):
            break
        floor = my_list[index]
        print(f"floor= {floor}")
        if floor >= key:
            eggs -= 1
            print(f"eggs= {eggs}")
            for j in range(eggs + 1):
                turn += 1
                print("# # # # #")
                print(f"j= {j}")
                print(f"turn+1= {turn}= tedade partabha")
                print(f"index= {index}")
                print(f"floor= {floor}")
                print(f"eggs= {eggs}")
                if floor == key:
                    return turn
                floor = my_list[index - (j + 1)]
                eggs -= 1
                if eggs < 0:
                    return "not enough eggs"
    return -1
my_list = [i for i in range(101)]
key = 79
eggs = 3
print(search(key, my_list, eggs))
