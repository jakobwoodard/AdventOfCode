# --- Day 6: Guard Gallivant ---

# The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

# You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

# Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

# You start by making a map (your puzzle input) of the situation. For example:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.
# Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

# ....#.....
# ....^....#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...
# Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

# ....#.....
# ........>#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...
# Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#......v.
# ........#.
# #.........
# ......#...
# This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#v..
# By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

# ....#.....
# ....XXXXX#
# ....X...X.
# ..#.X...X.
# ..XXXXX#X.
# ..X.X.X.X.
# .#XXXXXXX.
# .XXXXXXX#.
# #XXXXXXX..
# ......#X..
# In this example, the guard will visit 41 distinct positions on your map.

# Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
    

with open('day6_input.txt', 'r') as f:
    lines = f.readlines()
    matrix = []
    for line in lines:
        temp = list(line)
        matrix.append(temp)
    i_start, j_start = 0, 0
    
    # get our starting spot
    for i, row in enumerate(matrix):
        for j, spot in enumerate(row):
            if spot == '^':
                i_start = i
                j_start = j
    
    facing = 'up'
    total_spaces = 1
    i = i_start
    j = j_start
    escaped = False
    while not escaped:
        match facing:
            case 'up':
                if (i - 1 < 0):
                    escaped = True
                elif (matrix[i - 1][j] == '.'):
                    matrix[i - 1][j] = 'X'
                    total_spaces+=1
                    i -=1
                elif (matrix[i - 1][j] == '#'):
                    facing = 'right'
                else:
                    i-=1 # already visited
            case 'right':
                if (j + 1 >= len(matrix[i])):
                    escaped = True
                elif (matrix[i][j + 1] == '.'):
                    matrix[i][j+1] = 'X'
                    total_spaces+=1
                    j+=1
                elif (matrix[i][j + 1] == '#'):
                    facing = 'down'
                else:
                    j+=1 # already visited
            case 'down':
                if (i + 1 >= len(matrix)):
                    escaped = True
                elif (matrix[i + 1][j] == '.'):
                    matrix[i+1][j] = 'X'
                    total_spaces+=1
                    i+=1
                elif (matrix[i + 1][j] == '#'):
                    facing = 'left'
                else:
                    i+=1 # already visited
            case 'left':
                if (j - 1 < 0 ):
                    escaped = True
                elif (matrix[i][j - 1] == '.'):
                    matrix[i][j-1] = 'X'
                    total_spaces+=1
                    j-=1
                elif (matrix[i][j - 1] == '#'):
                    facing = 'up'
                else: # already visited
                    j-=1
            case _:
                print("Something went wrong")
    print(total_spaces)
    
