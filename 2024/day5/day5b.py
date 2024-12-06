# --- Part Two ---

# While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

# For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13.
# After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

# Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?

### Chekcks the current order of prints for an INVALID order. Returns the INVALID order if found. NONE if not
def checkOrder(cur_order, order_rules):
    prev_values = []
    cur_order[-1] = cur_order[-1].strip()
    for value in cur_order:
        if value in order_rules: # if numbers need to be printed before the current number
            for rule in order_rules[value]:
                if str(rule) in prev_values: 
                    return cur_order # return only ones that dont work
        prev_values.append(value)
    return False # if it does work, don't return anything useful

### Fixes an incorrect order and returns the new, fixed order.
def fixOrder(cur_order, order_rules):
    fixed_order = list(cur_order)
    should_reset = False
    while checkOrder(fixed_order, order_rules): # while we are still getting an output from checkOrder, i.e. while the order is still wrong
        prev_values = []
        for value in fixed_order: # get the the next value
            if value in order_rules: # if a different value need to be printed before the current value
                for rule in order_rules[value]: # check that all the rules are followed
                    if str(rule) in prev_values: # if a rule has been broken
                        should_reset = True # we should start the while loop back again
                        # move the value to the index before the rule was broken
                        fixed_order.insert(fixed_order.index(str(rule)), fixed_order.pop(fixed_order.index(value)))
                        break # we made a change, break out
                if should_reset:
                    should_reset = False
                    break
            prev_values.append(value)
    return fixed_order
    

with open('day5_input.txt', 'r') as f:
    order_rules = {} # dict representation of order rules associated by a number for the key and a list of values that must occur AFTER the number as the value
    lines = f.readlines()
    correct_updates = []
    sum = 0
    for line in lines:
        if '|' in line:
            x, y = line.split('|')
            if x in order_rules:    
                order_rules[x].append(int(y))
            else:
                order_rules[x] = [int(y)]
        elif ',' in line:
            incor_order = checkOrder([x for x in line.split(",")], order_rules)
            if incor_order:
                fixed_order = fixOrder(incor_order, order_rules)
                sum+= int(fixed_order[(len(fixed_order) // 2)])
    print(sum)