# --- Part Two ---

# The reindeer spends a few minutes reviewing your hiking trail map before realizing something, disappearing for a few minutes, and finally returning with yet another slightly-charred piece of paper.

# The paper describes a second way to measure a trailhead called its rating. A trailhead's rating is the number of distinct hiking trails which begin at that trailhead. For example:

# .....0.
# ..4321.
# ..5..2.
# ..6543.
# ..7..4.
# ..8765.
# ..9....
# The above map has a single trailhead; its rating is 3 because there are exactly three distinct hiking trails which begin at that position:

# .....0.   .....0.   .....0.
# ..4321.   .....1.   .....1.
# ..5....   .....2.   .....2.
# ..6....   ..6543.   .....3.
# ..7....   ..7....   .....4.
# ..8....   ..8....   ..8765.
# ..9....   ..9....   ..9....
# Here is a map containing a single trailhead with rating 13:

# ..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....
# This map contains a single trailhead with rating 227 (because there are 121 distinct hiking trails that lead to the 9 on the right edge and 106 that lead to the 9 on the bottom edge):

# 012345
# 123456
# 234567
# 345678
# 4.6789
# 56789.
# Here's the larger example from before:

# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# Considering its trailheads in reading order, they have ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5. The sum of all trailhead ratings in this larger example topographic map is 81.

# You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper and is using them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?


# Similar to part a's findPath, but just without searching for unique ends.
def findPath(matrix, i, j):
    cur_number = int(matrix[i][j])
    sum = 0
    
    # Base case, if we found the last value in the path
    if int(cur_number) == 9:
        return 1
    # Look right for the next value
    if j + 1 < len(matrix[i]):
        if matrix[i][j + 1] == str(cur_number + 1):
            sum+= findPath(matrix, i, j+1)
    # Look left for next value
    if j - 1 >= 0:
        if matrix[i][j - 1] == str(cur_number + 1):
            sum+= findPath(matrix, i, j - 1)
    # Look up for the vaule
    if i - 1 >= 0:
        if matrix[i - 1][j] == str(cur_number + 1):
            sum+= findPath(matrix, i - 1, j)
    # Look down for the value
    if i + 1 < len(matrix):
        if matrix[i + 1][j] == str(cur_number + 1):
            sum+= findPath(matrix, i + 1, j)
            
    return sum

if __name__ == '__main__':
    with open('day10_input.txt', 'r') as f:
        map_matrix = []
        lines = f.readlines()
        
        # Build our matrix
        for line in lines:
            map_matrix.append(line.strip())
        
        # Look for a '0' to start processing
        sum = 0
        for i, line in enumerate(map_matrix):
            for j, num in enumerate(line):
                if num == '0':
                    sum += findPath(map_matrix, i, j)
        print(sum)