import random


def tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Welcome to tic tac toe")
    print('1: PvP')
    print('2: PvC')
    print('3: Quit')
    input1 = input('Please select 1, 2, or 3: ')
    while True:
        if input1 == '1':
            input2 = input("Player 1 Please Select a Row (0, 1, 2): ")
            input3 = input("Player 1 Please Select a Column (0, 1, 2): ")
            while board[int(input2)][int(input3)] != ' ':
                print('Already Taken. Please Try Again')
                input2 = input("Player 1 Please Select a Row (0, 1, 2): ")
                input3 = input("Player 1 Please Select a Column (0, 1, 2): ")
            else:
                board[int(input2)][int(input3)] = 'X'
                print(board[0])
                print(board[1])
                print(board[2])
                if check_winner(board) is False:
                    break
            input4 = input("Player 2 Please Select a Row (0, 1, 2): ")
            input5 = input("Player 2 Please Select a Column (0, 1, 2): ")
            while board[int(input4)][int(input5)] != ' ':
                print('Error. Please Try Again')
                input4 = input("Player 2 Please Select a Row (0, 1, 2): ")
                input5 = input("Player 2 Please Select a Column (0, 1, 2): ")
            else:
                board[int(input4)][int(input5)] = 'O'
                print(board[0])
                print(board[1])
                print(board[2])
                if check_winner(board) is False:
                    break
        elif input1 == '2':
            difficulty = input("Please select difficulty (easy or hard): ")
            if difficulty == 'easy':
                input2 = input("Player 1 Please Select a Row (0, 1, 2): ")
                input3 = input("Player 1 Please Select a Column (0, 1, 2): ")
                while board[int(input2)][int(input3)] != ' ':
                    print('Already Taken. Please Try Again')
                    input2 = input("Player 1 Please Select a Row (0, 1, 2): ")
                    input3 = input("Player 1 Please Select a Column (0, 1, 2): ")
                else:
                    board[int(input2)][int(input3)] = 'X'
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    if check_winner(board) is False:
                        break
                while True:
                    row = random.randint(0, 2)
                    column = random.randint(0, 2)
                    if board[row][column] == ' ':
                        board[row][column] = 'O'
                        print(board[0])
                        print(board[1])
                        print(board[2])
                        break
                if check_winner(board) is False:
                    break
        elif input1 == '3':
            print("Please Play Again!")
            break
        else:
            print('Invalid Input. Please Try Again')
            break


def check_winner(board: list[list[str]]):
    if board[0] == ['X', 'X', 'X']:
        print("X's Win!")
        return False
    elif board[0] == ['O', 'O', 'O']:
        print("O's Win!")
        return False
    elif board[1] == ['X', 'X', 'X']:
        print('You are a winner')
        return False
    elif board[1] == ['O', 'O', 'O']:
        print("O's Win!")
        return False
    elif board[2] == ['X', 'X', 'X']:
        print('You are a winner')
        return False
    elif board[2] == ['O', 'O', 'O']:
        print("O's Win!")
        return False
    elif board[2][0] == board[1][0] == board[0][0] == 'X':
        print("X's Win!")
        return False
    elif board[2][0] == board[1][0] == board[0][0] == 'O':
        print("O's Win!")
        return False
    elif board[2][1] == board[1][1] == board[0][1] == 'X':
        print("X's Win!")
        return False
    elif board[2][1] == board[1][1] == board[0][1] == 'O':
        print("O's Win!")
        return False
    elif board[1][2] == board[0][2] == board[2][2] == 'X':
        print("X's Win!")
        return False
    elif board[1][2] == board[0][2] == board[2][2] == 'O':
        print("O's Win!")
        return False
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        print("X's Win!")
        return False
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        print("O's Win!")
        return False
    elif board[0][2] == board[1][1] == board[2][0] == 'X':
        print("X's Win!")
        return False
    elif board[0][2] == board[1][1] == board[2][0] == 'O':
        print("O's Win!")
        return False
    elif ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        print("It's a Tie!")
        return False
    return True


tic_tac_toe()
