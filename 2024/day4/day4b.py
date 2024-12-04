# The Elf looks quizzically at you. Did you misunderstand the assignment?

# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

# Here's the same example from before, but this time all of the X-MASes have been kept instead:

# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.

# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?


def checkDownRight(matrix, i, j):
    if i + 1 >= len(matrix) or j + 1 >= len(matrix[i]) or i - 1 < 0 or j - 1 < 0: return 0
    if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S': return 1
    return 0

def checkDownLeft(matrix, i, j):
    if i + 1 >= len(matrix) or j + 1 >= len(matrix[i]) or i - 1 < 0 or j - 1 < 0: return 0
    if matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S': return 1
    return 0

def checkUpRight(matrix, i, j):
    if i + 1 >= len(matrix) or j + 1 >= len(matrix[i]) or i - 1 < 0 or j - 1 < 0: return 0
    if matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S': return 1
    return 0

def checkUpLeft(matrix, i , j):
    if i + 1 >= len(matrix) or j + 1 >= len(matrix[i]) or i - 1 < 0 or j - 1 < 0: return 0
    if matrix[i+1][j+1] == 'M' and matrix[i-1][j-1] == 'S': return 1
    return 0

def checkAll(matrix, i, j):
    if checkDownRight(matrix, i, j):
        return checkUpRight(matrix, i, j) + checkDownLeft(matrix, i, j)
    elif checkDownLeft(matrix, i, j):
        return checkDownRight(matrix, i, j) + checkUpLeft(matrix, i, j)
    elif checkUpLeft(matrix, i, j):
        return checkUpRight(matrix, i, j) + checkDownLeft(matrix, i, j)
    elif checkUpRight(matrix, i, j):
        return checkDownRight(matrix, i, j) + checkUpLeft(matrix, i, j)
    else:
        return 0

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
            if char == 'A':                
                total += checkAll(matrix, i, j)
    print(total)