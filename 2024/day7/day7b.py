# --- Part Two ---

# The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

# The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

# Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

# 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
# 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
# 192: 17 8 14 can be made true using 17 || 8 + 14.
# Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

# Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?

from itertools import product


def makeSum(sum, numbers):   
    combos = []
    for combo in product(['+', '*', '||'], repeat=len(numbers) - 1):
        combos.append(combo)
    for combo in combos:
        cur_total = 0
        for i, operation in enumerate(combo):
            if operation == '+':
                if i == 0:   
                    cur_total+= int(numbers[i]) + int(numbers[i + 1])
                else: 
                    cur_total+= int(numbers[i + 1])
            elif operation == '*':
                if i == 0:    
                    cur_total+= int(numbers[i]) * int(numbers[i + 1])
                else:
                    cur_total*= int(numbers[i + 1])
            else:
                if i ==0:
                    cur_total+=int(numbers[i] + numbers[i + 1])
                else:
                    cur_total = int(str(cur_total) + numbers[i+1])
            ### Small optimization, we can quit compute if our total is already too high
            if cur_total > int(sum):
                break
        ### We did the correct combo, return the total
        if cur_total == int(sum):
            return cur_total 
    ## Correct combo was not found so is not possible, return 0
    return 0


with open('day7_input.txt', 'r') as f:
    lines = f.readlines()
    sums = []
    numbers = []
    for line in lines:
        split_line = line.split(':')
        sums.append(split_line[0])
        numbers.append(tuple(split_line[1].strip().split(' ')))
    total = 0
    for i, sum in enumerate(sums):
        matched_sum = makeSum(sum, numbers[i])
        total+= matched_sum
    print(total)