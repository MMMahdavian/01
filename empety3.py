def search(key, my_list, eggs):
    for turn in range((len(my_list) + 2) // 3):
        index = 3 * turn + 1
        if index >= len(my_list):
            break
        floor = my_list[index]
        if floor >= key:
            eggs -= 1
            for j in range(eggs + 1):
                turn += 1
                if floor == key:
                    return turn
                floor = my_list[index - (j + 1)]
                eggs -= 1