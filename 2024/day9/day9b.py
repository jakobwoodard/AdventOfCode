# --- Part Two ---

# Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file system fragmentation was a bad idea?

# The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving whole files instead.

# This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

# The first example from above now proceeds differently:

# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..
# The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

# Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?
      
### Fits whole file blocks into the empty spaces, starting from the right-most file      
def wholeFiles(disk_map):

    r_pointer = len(disk_map) - 1
    while r_pointer > 0:
        block_size = 0
        while disk_map[r_pointer] == '.':
            r_pointer-=1
        cur_page = disk_map[r_pointer]
        while disk_map[r_pointer] == cur_page:
            block_size+=1
            r_pointer-=1
        temp = getAvailableSpace(disk_map, block_size, cur_page, r_pointer)
        
        # if we found a spot to put the value
        if not temp == 0:
            disk_map = temp
            
        
    return disk_map
    
               
### Checks to see if there is an available spot for a file 
def getAvailableSpace(disk_map, block_size, cur_page, r_pointer):
    i = 0
    available_space = 0
    while i < len(disk_map):
        if disk_map[i] == '.':
            available_space+=1
        else:
            available_space = 0
        i+=1
            
        # if we find enough available space, transfer
        if available_space >= block_size:
            if i > r_pointer + 1:
                return 0
            # Remove all values of the current page from the list using list comprehension
            disk_map = ['.' if x == cur_page else x for x in disk_map]
            # Put the new values in the list
            for j in range(available_space):
                disk_map[i - j - 1] = cur_page
            return disk_map
    return 0
        
            
            
            


if __name__ == '__main__':
    with open('day9_input.txt', 'r') as f:
        line = f.readline().strip()
        length = len(line)
        
        i = 0
        cur_id = 0
        disk_map = []
        # read_block is true if we are getting the block size, false if we are reading how many empty spaces
        read_block = True
        while i < length:
            if read_block:
                block_size = int(line[i])
                for j in range(block_size):
                    disk_map.append(cur_id)
                cur_id+= 1
                read_block = False
            else:
                free_space = int(line[i])
                for j in range(free_space):
                    disk_map.append('.')
                read_block = True
            i+= 1
        disk_map = wholeFiles(disk_map)
        sum = 0
        for i, value in enumerate(disk_map):
            if not value == '.':
                sum += (i * int(value))
        print(sum)
        