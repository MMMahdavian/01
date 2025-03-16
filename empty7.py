def check_winner(board, symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol \
        or board[0][i] == board[1][i] == board[2][i] == symbol:
            print(f"player{symbol} won!!!")
            exit()
    if board[0][0] == board[1][1] == board[2][2] == symbol \
    or board[0][2] == board[1][1] == board[2][0] == symbol:
        print(f"player{symbol} won!!!")
        exit()
