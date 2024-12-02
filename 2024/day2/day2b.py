# --- Part Two ---

# The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

# More of the above example's reports are now safe:

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# Thanks to the Problem Dampener, 4 reports are actually safe!

# Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

# NOTE: dapenerActive = true if second run, false if first
def checkReport(report, dapenerActive=False):
    cur_direction = 0
    prev_direction = 0
    for i, data in enumerate(report):
        if i == 0:
            prev = data
            continue
        else:
            cur_direction = (prev - data) * -1
            if cur_direction == 0:
                if dapenerActive:
                    return False
                else:
                    # check report if we take out the current index, first or second index, or last index
                    # NOTE we check the first, second and last indicies b/c our switch only accounts for a problem in the middle of the list
                    # we check the second index b/c all we do in our first pass is set prev data and direction
                    return (checkReport(report[:i] + report[i+1:], True) or checkReport(report[:-1], True) or checkReport(report[1:], True) or checkReport(report[:1] + report[2:], True))
            elif abs(cur_direction) > 3:
                if dapenerActive:
                    return False
                else:
                    # check report if we take out the current index, first or second index, or last index
                    # NOTE we check the first, second and last indicies b/c our switch only accounts for a problem in the middle of the list
                    # we check the second index b/c all we do in our first pass is set prev data and direction
                    return (checkReport(report[:i] + report[i+1:], True) or checkReport(report[:-1], True) or checkReport(report[1:], True) or checkReport(report[:1] + report[2:], True))
            cur_direction = cur_direction / abs(cur_direction)
            if i == 1:
                prev = data
                prev_direction = cur_direction
                continue
            else:
                if prev_direction != cur_direction:
                    if dapenerActive:
                        return False
                    else:
                        # check report if we take out the current index, first or second index, or last index
                        # NOTE we check the first, second and last indicies b/c our switch only accounts for a problem in the middle of the list
                        # we check the second index b/c all we do in our first pass is set prev data and direction
                        return (checkReport(report[:i] + report[i+1:], True) or checkReport(report[:-1], True) or checkReport(report[1:], True) or checkReport(report[:1] + report[2:], True))
        prev_direction = cur_direction
        prev = data
    return True

with open('day2_input.txt', 'r') as f:
    lists = []
    lines = f.readlines()
    for i, line in enumerate(lines):
        levels = line.split()
        levels_numbers = [int(x) for x in levels]
        lists.append(levels_numbers)
    safe_reports = 0
    for report in lists:
        if checkReport(report):
            safe_reports+= 1           
    print(safe_reports) 