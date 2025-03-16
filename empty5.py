# A = [int(i) for i in input().split()]
# B = [[A[i], A[i + 1], A[i + 2]] for i in range(0, 9, 3)]
# print(B)
# print(list(range(0, 10, 3)))

A = [list(range(1 , 4)) , list(range(4 , 7)) , list(range(7 , 10))]
for turn in range(9):
    if turn % 2 == 0:
        while True:
            try:
                x = int(input("(*)player1: "))
                break
            except ValueError:
                print("enter a number")
        if A[(x - 1) // 3][(x + 2) % 3] == "#":
            print("error")
            exit()
        else:
            A[(x - 1) // 3][(x + 2) % 3] = "*"
    else:
        while True:
            try:
                x = int(input("(#)player2: "))
                break
            except ValueError:
                print("enter a number")
        if A[(x - 1) // 3][(x + 2) % 3] == "*":
            print("error")
            exit()
        else:
            A[(x - 1) // 3][(x + 2) % 3] = "#"
    for j in A:
        print(" ".join(map(str, j)))
    for k in range(3):
        if A[k][0] == A[k][1] == A[k][2] == "*"\
        or A[0][k] == A[1][k] == A[2][k] == "*":
            print("player1 won!!!")
            exit()
        if A[0][0] == A[1][1] == A[2][2] == "*"\
        or A[0][2] == A[1][1] == A[2][0] == "*":
            print("player1 won!!!")
            exit()
    for k in range(3):
        if (A[k][0] == A[k][1] == A[k][2] == "#" or
        A[0][k] == A[1][k] == A[2][k] == "#"):
            print("player2 won!!!")
            exit()
        if (A[0][0] == A[1][1] == A[2][2] == "#" or
        A[0][2] == A[1][1] == A[2][0] == "#"):
            print("player2 won!!!")
            exit()