# --- Part Two ---

# While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

# Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

# Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

# To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

# In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

# Option one, put a printing press next to the guard's starting position:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ....|..#|.
# ....|...|.
# .#.O^---+.
# ........#.
# #.........
# ......#...
# Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ......O.#.
# #.........
# ......#...
# Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----+O#.
# #+----+...
# ......#...
# Option four, put an alchemical retroencabulator near the bottom left corner:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ..|...|.#.
# #O+---+...
# ......#...
# Option five, put the alchemical retroencabulator a bit to the right instead:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ....|.|.#.
# #..O+-+...
# ......#...
# Option six, put a tank of sovereign glue right next to the tank of universal solvent:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----++#.
# #+----++..
# ......#O..
# It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

# You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?

import copy

def checkLoop(matrix, i, j):
    escaped = False
    prev_space_direction = {} # dict to hold previous direction when on matrix square. key = str(i) + ' ' + str(j). value = direction
    matrix[i_start][j_start] = 'X'
    facing = 'up'
    while not escaped:
        match facing:
            case 'up':
                if (i - 1 < 0):
                    escaped = True
                    break
                elif (matrix[i - 1][j] == '.'):
                    if str(i) + ' ' + str(j) in prev_space_direction:
                        if facing in prev_space_direction[str(i) + ' ' + str(j)]:
                            return 1
                        else:
                            prev_space_direction[str(i) + ' ' + str(j)].append(facing)
                    prev_space_direction[str(i) + ' ' + str(j)] = [facing]
                    i -=1
                elif (matrix[i - 1][j] == '#'):
                    facing = 'right'
                else:
                    i-=1 # already visited
            case 'right':
                if (j + 1 >= len(matrix[i])):
                    escaped = True
                    break
                elif (matrix[i][j + 1] == '.'):
                    if str(i) + ' ' + str(j) in prev_space_direction:
                        if facing in prev_space_direction[str(i) + ' ' + str(j)]:
                            return 1
                        else:
                            prev_space_direction[str(i) + ' ' + str(j)].append(facing)
                    prev_space_direction[str(i) + ' ' + str(j)] = [facing]
                    j+=1
                elif (matrix[i][j + 1] == '#'):
                    facing = 'down'
                else:
                    j+=1 # already visited
            case 'down':
                if (i + 1 >= len(matrix)):
                    escaped = True
                    break
                elif (matrix[i + 1][j] == '.'):
                    if str(i) + ' ' + str(j) in prev_space_direction:
                        if facing in prev_space_direction[str(i) + ' ' + str(j)]:
                            return 1
                        else:
                            prev_space_direction[str(i) + ' ' + str(j)].append(facing)
                    prev_space_direction[str(i) + ' ' + str(j)] = [facing]
                    i+=1
                elif (matrix[i + 1][j] == '#'):
                    facing = 'left'
                else:
                    i+=1 # already visited
            case 'left':
                if (j - 1 < 0 ):
                    escaped = True
                    break
                elif (matrix[i][j - 1] == '.'):
                    if str(i) + ' ' + str(j) in prev_space_direction:
                        if facing in prev_space_direction[str(i) + ' ' + str(j)]:
                            return 1
                        else:
                            prev_space_direction[str(i) + ' ' + str(j)].append(facing)
                    prev_space_direction[str(i) + ' ' + str(j)] = [facing]
                    j-=1
                elif (matrix[i][j - 1] == '#'):
                    facing = 'up'
                else: # already visited
                    j-=1
            case _:
                print("Something went wrong")
    return 0


if __name__ == '__main__':
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
        
        ### BRUTE FORCE TIME. IF GUARD GOES OVER SAME SPOT IN SAME DIRECTION ONCE THEN WE HAVE A LOOP ###
        ### PUT OBSTACLE ON EVERY SPOT AND SEE IF ANYTHING CHANGES ###
        facing = 'up'
        total_loops = 0
                
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix_copy = copy.deepcopy(matrix)
                matrix_copy[i][j] = '#'
                total_loops+= checkLoop(matrix_copy, i_start, j_start)
        
        
        
        print(total_loops)