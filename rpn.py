#! /usr/bin/env python3
import helper
import operator
import math
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': helper.percent,
    '^': operator.pow,
    '//': operator.floordiv,
    '!': math.factorial,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.invert,
}

last = 0
repeat = 0

def calculate(arg):
    stack = []
    global last, repeat
    for token in arg.split():
        repeat = 0
        try:
            token = float(token)
            stack.append(token)
        except ValueError:
            try:
                function = operators[token]
                if token =='!' and len(stack) != 1:
                        raise KeyError("Repeat")
            except KeyError:
                if token == ':ans':
                    stack.append(last)
                if token == '!' and len(stack) != 1:
                    repeat = 1
                    numElt = len(stack)
                    newArg = ' '.join(str(e) for e in stack)
                    newArg = newArg + (op * (numElt - 1))
            else:
                arg2 = stack.pop()
                if token != '~' and token != '!':
                    arg1 = stack.pop()
                if token == '%':
                    stack.append(arg1)
                if token == '&' or token == '|' or token == '~' or token == '!':
                    arg2 = int(arg2)
                    if token != '~' and token != '!':
                        arg1 = int(arg1)
                if token == '~' or token == '!':
                    result = function(arg2)
                else:
                    result = function(arg1, arg2)
                op = ' ' + token
                if repeat != 1:
                    stack.append(result)
            if repeat == 1:
                result = calculate(newArg)
                del stack[:] 
                stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    last = stack.pop()
    return last

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
