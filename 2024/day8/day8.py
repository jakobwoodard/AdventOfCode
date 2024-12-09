# --- Day 8: Resonant Collinearity ---

# You find yourselves on the roof of a top-secret Easter Bunny installation.

# While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

# Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

# So, for these two antennas with frequency a, they create the two antinodes marked with #:

# ..........
# ...#......
# ..........
# ....a.....
# ..........
# .....a....
# ..........
# ......#...
# ..........
# ..........
# Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, but two are off the right side of the map, so instead it adds only two:

# ..........
# ...#......
# #.........
# ....a.....
# ........a.
# .....a....
# ..#.......
# ......#...
# ..........
# ..........
# Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However, antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A creates no antinodes but has a lowercase-a-frequency antinode at its location:

# ..........
# ...#......
# #.........
# ....a.....
# ........a.
# .....a....
# ..#.......
# ......A...
# ..........
# ..........
# The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an antinode overlapping the topmost A-frequency antenna:

# ......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.
# Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that contain an antinode within the bounds of the map.

# Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?

from itertools import combinations

if __name__ == '__main__':
    with open('day8_input_small.txt', 'r') as f:
        nodes = {} # dict representation of all nodes with the key being the node char and the value being the list of index values representing each node
        lines = f.readlines()
        i_max = len(lines)
        j_max = len(lines[0])
        # Get all of the node values
        for i, line in enumerate(lines):
            for j, char in enumerate(line.strip()):
                if not char == '.':
                    if not char in nodes:
                        nodes[char] = [tuple([i, j])]
                    else:                       
                        nodes[char].append(tuple([i, j]))
        # Create the antinodes
        anti_nodes = 0
        anti_node_locations = []
        for type, location in nodes.items():
            for index in combinations(location, r=2):
                anti_node_i_distance = index[0][0] - index[1][0]
                anti_node_j_distance = index[0][1] - index[1][1]
                # try to add an anti_node, check bounds first
                if index[0][0] + anti_node_i_distance >= 0 and index[0][1] + anti_node_j_distance >= 0:
                    anti_node_locations.append(tuple([index[0][0] + anti_node_i_distance, index[0][1] + anti_node_j_distance]))
                    anti_nodes+=1
                if index[1][0] - anti_node_i_distance < i_max and index[1][1] - anti_node_j_distance < j_max:
                    anti_node_locations.append(tuple([index[1][0] - anti_node_i_distance, index[1][1] - anti_node_j_distance]))
                    anti_nodes+=1
                    
        count = 0
        input_matrix = []
        for i in range(0, len(lines)):
            input_matrix.append(list())
            for j in range(0, len(lines[0]) - 1):
                new_tuple = tuple([i, j])
                if new_tuple in anti_node_locations:
                    count += 1
                    input_matrix[i].append('#')
                else:
                    input_matrix[i].append('.')
        print(count)
                    