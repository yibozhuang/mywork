def evalRPN(tokens):
    stack = []

    ops = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y
    }
    for s in tokens:
        try:
            stack.append( float(s) )
        except:
            stack.append( int( ops[s]( stack.pop(-2), stack.pop(-1) ) ) )

    return int(stack[-1])

print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
