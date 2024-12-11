# Same as part 1 but with 75 blinks instead

from functools import cache

@cache
def transform(runs, number):
    sum = 0
    if runs <=  0:
        return 1
    if number == 0:
        sum += transform(runs - 1, number + 1)
    elif len(str(number)) % 2 == 0:
        sum += transform(runs - 1, int(str(number)[:len(str(number)) // 2]))
        sum += transform(runs - 1, int(str(number)[len(str(number)) // 2:])) # string representation of int representation of string value to eliminate trailing 0s
    else:
        sum += transform(runs - 1, number * 2024)
    return sum
    
    

if __name__ == '__main__':
    with open('day11_input.txt', 'r') as f:
        numbers = f.readline().strip().split(' ')
        sum = 0
        for value in numbers:
            sum += transform(75, int(value))
        print(sum)