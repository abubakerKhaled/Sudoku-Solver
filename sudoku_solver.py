def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and  i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8: 
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + ' ', end='')


def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col

    return None, None


def is_valid(puzzle, guess, row, col):
    # for i in range(9):
    #     if puzzle[row][i] == guess:
    #         return False
    
    # for i in range(9):
    #     if puzzle[i][col] == guess:
    #         return False
    
    
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True


def sudoku_solver(puzzle):
    
    row, col = find_next_empty(puzzle)

    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            
            if sudoku_solver(puzzle):
                return True
        
        # print(np.matrix(puzzle))
        
        # backtrack and set another guess 
        puzzle[row][col] = 0
        
    # if none of the numbers that we try didn't work, then this puzzle is UNSOLVABLE
    return False


if __name__ == "__main__":
    sudoku = [
        [1, 0, 7, 0, 0, 6, 4, 5, 0],
        [0, 2, 5, 3, 4, 0, 0, 0, 8],
        [0, 6, 0, 0, 0, 1, 0, 7, 0],
        [0, 5, 3, 0, 0, 0, 0, 2, 9],
        [6, 1, 0, 0, 0, 9, 8, 0, 0],
        [0, 0, 0, 6, 0, 2, 0, 0, 7],
        [0, 0, 1, 0, 9, 3, 2, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 7, 8, 5, 9, 1]
    ]
    
    print_sudoku(sudoku)
    sudoku_solver(sudoku)
    print("--After Solution--")
    print_sudoku(sudoku)
