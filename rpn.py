#!/usr/bin/env python3
import operator
from datetime import datetime
import sys
#from termcolor import colored

ops = {
    '+': operator.add,
    '-': operator.sub,
}

def calculate(myarg):
    stack = list()


    for token in myarg.split():
        
        try:
            stack.append(int(token))

        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            
            result = function(arg1, arg2)
            #print(result)
           # print(colored(result, 'red'))
            stack.append(result)

    return stack.pop()

def main():
    
    while True:
        input_text = input("rpn calc> ")
        result = calculate(input_text)

if __name__ == '__main__':
    main()