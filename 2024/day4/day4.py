
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?

def checkUp(matrix, i , j):
    if i - 3 < 0: return 0
    if matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S': return 1
    return 0

def checkDown(matrix, i , j):
    if i + 3 >= len(matrix): return 0
    if matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S': return 1
    return 0

def checkLeft(matrix, i , j):
    if j - 3 < 0: return 0
    if matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S': return 1
    return 0

def checkRight(matrix, i , j):
    if (j + 3 >= len(matrix[i])): return 0
    if matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S': return 1
    return 0

def checkUpLeft(matrix, i , j):
    if (i - 3 < 0) or (j - 3 < 0): return 0
    if matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S': return 1
    return 0

def checkUpRight(matrix, i , j):
    if (i - 3 < 0) or (j + 3 >= len(matrix[i])): return 0
    if matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S': return 1
    return 0

def checkDownLeft(matrix, i , j):
    if (i + 3 >= len(matrix)) or (j - 3 < 0): return 0
    if matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S': return 1
    return 0

def checkDownRight(matrix, i , j):
    if (i + 3 >= len(matrix)) or (j + 3 >= len(matrix[i])): return 0
    if matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S': return 1
    return 0

def checkAll(matrix, i , j):
    return checkUp(matrix, i , j) + checkDown(matrix, i , j) + checkLeft(matrix, i , j) + checkRight(matrix, i , j) + checkUpLeft(matrix, i , j) + checkUpRight(matrix, i , j) + checkDownLeft(matrix, i , j) + checkDownRight(matrix, i , j)
    
    

with open('day4_input.txt', 'r') as f:
    lines = f.readlines()
    matrix = []
    # load our array with individual maxtrix values
    for line in lines:
        col = []
        for char in line:
            col.append(char)
        matrix.append(col) 
    
    total = 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == 'X':                
                total += checkAll(matrix, i, j)
    print(total)