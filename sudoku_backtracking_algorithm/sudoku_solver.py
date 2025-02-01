from tkinter import *
from tkinter import font

enterByHand = False

if enterByHand:
    root = Tk()
    bold_font = font.Font(weight="bold")
    root.title("9x9 Grid")

    box_entries = [[None for _ in range(9)] for _ in range(9)]
    board = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if ((i % 3 == 0) and (j % 3 == 0)):
                entry = Entry(root, width=5, bg="red", fg="purple", borderwidth=5, font=bold_font)
            elif i % 3 == 0:
                entry = Entry(root, width=5, bg="blue", fg="purple", borderwidth=5, font=bold_font)
            elif j % 3 == 0:
                entry = Entry(root, width=5, bg="blue", fg="purple", borderwidth=5, font=bold_font)
            else:
                entry = Entry(root, width=5, bg="cyan", fg="purple", borderwidth=5, font=bold_font)
            entry.insert(0, "0")  # Set the default value to "0"
            entry.grid(row=i, column=j)
            box_entries[i][j] = entry


    def click():
        for i in range(9):
            for j in range(9):
                value = box_entries[i][j].get()
                if value.isdigit():
                    board[i][j] = int(value)
                else:
                    board[i][j] = 0
        print(f"The starting position of the sudoku is:\n{board}")


    button = Button(root, text="Submit", command=click)
    button.grid(row=10, column=4, columnspan=2)
    root.mainloop()
else:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_board_valid(board, number, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check subgrid
    start_row, start_col = (position[0] // 3) * 3, (position[1] // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number and position != (i, j):
                return False

    return True



def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if is_board_valid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = 0
    return False


print_board(board)
solve(board)
print("----------------------------------------------------------------")
print_board(board)