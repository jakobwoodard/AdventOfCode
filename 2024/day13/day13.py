from sympy import symbols, Eq, solve 
from sympy import Integer
import re

def solver(x_symbol, y_symbol, x1, x2, y1, y2, sum1, sum2):
    
    # defining equations 
    eq1 = Eq((x1 * x_symbol + x2 * y_symbol), sum1) 
    eq2 = Eq((y1 * x_symbol + y2 * y_symbol), sum2) 
    return solve((eq1, eq2), (x, y))

if __name__ == '__main__':
    # defining symbols used in equations 
    # or unknown variables
    ten_trillion = 10000000000000
    
    with open('day13_input.txt', 'r') as f:
        lines = f.readlines()
        pattern = ""
        x1 = x2 = y1 = y2 = sum1 = sum2 = 0
        total = 0
        for line in lines:
            if "Button A" in line:
                pattern = r'X\+[0-9]{1,3}'
                match = re.findall(pattern, line)
                new_match = match[0][2:]
                x1 = int(new_match)
                pattern = r'Y\+[0-9]{1,3}'
                match = re.findall(pattern, line)
                new_match = match[0][2:]
                y1 = int(new_match)
            elif "Button B" in line:
                pattern = r'X\+[0-9]{1,3}'
                match = re.findall(pattern, line)
                new_match = match[0][2:]
                x2 = int(new_match)
                pattern = r'Y\+[0-9]{1,3}'
                match = re.findall(pattern, line)
                new_match = match[0][2:]
                y2 = int(new_match)
            elif "Prize" in line:
                pattern = r'X\=\d+, Y=\d+'
                match = re.findall(pattern, line) # match holds x=#### y=####
                pattern = r'X\=\d+'
                x_match = re.findall(pattern, match[0])
                pattern = r'Y=\d+'
                y_match = re.findall(pattern, match[0])
                sum1 = int(x_match[0][2:]) + ten_trillion
                sum2 = int(y_match[0][2:]) + ten_trillion
            if x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0 and sum1 != 0 and sum2 != 0:
                x, y = symbols('x,y') 
                result = solver(x, y, x1, x2, y1, y2, sum1, sum2)
                if type(result[x]) == Integer and type(result[y] == Integer):
                    total+= (3 * result[x]) + result[y]
                x1 = x2 = y1 = y2 = sum1 = sum2 = 0
        print(f'total {total}')
                
    
     
        # x, y = symbols('x,y') 
        # test = solver(x, y, x1, x2, y1, y2, sum1, sum2)
        # if not (type(test[x]) == int or type(test[y]) == int):
        #     print("nothing found")