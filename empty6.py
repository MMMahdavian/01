A = [int(i) for i in input().split()]
bebrad_game = []
bebzad_game = []
for i in range(5):
    bebrad_game.append(A[2 * i])
    if 2 * i + 1 <= 8:
        bebzad_game.append(A[2 * i + 1])
marhale = 0
bebrad = 0
for i in range(3): #بررسی سطرها
    for j in range(3):
        if bebrad_game[i] == 3 * j + 1 and bebrad_game[i + 1] == 3 * j + 2 and bebrad_game[i + 2] == 3 * j + 3:
            marhale = 2 * i + 5
            bebrad = 1
            print(marhale)
            print(bebrad)
            break
for i in range(3): #بررسی ستون ها
    for j in range(3):
        if bebrad_game[i] == j + 1 and bebrad_game[i + 1] == j + 4 and bebrad_game[i + 2] == j + 7:
            marhale = 2 * i + 5
            bebrad = 1
            print(marhale)
            print(bebrad)
            break
for i in range(3): #بررسی قطر ها
    if (bebrad_game[i] == 1 and bebrad_game[i + 1] == 5 and bebrad_game[i + 2] == 9) or (bebrad_game[i] == 3 and bebrad_game[i + 1] == 5 and bebrad_game[i + 2] == 7):
        marhale = 2 * i + 5
        bebrad = 1
        print(marhale)
        print(bebrad)
        break