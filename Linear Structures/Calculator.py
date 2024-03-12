# Simple calculator which can evaluate a fully paranthesized arithmetic expression 

"""
"(1 + (1 - 1))" -> 1 

scope: 
    - assume fully paranthesized, and valid 
    - assume single digit integers 
    - support +, - 

stretch: 
    - check validity 
    - support multi-digit ints 

plan: 

s = []
for ch in expr: 
    if digit: push equivalent integer to stack 
    if operator: push function corresponding to operator 
    if ')': 
        pop last 3 values from stack, and evaluate operator function with two arguments
        push the result back 
    else: 
        continue 
return s.pop()    
"""

OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b
}

def calculate(expr):
    s = []
    for ch in expr: 
        if ch.isdigit():
            s.append(int(ch)) # TODO support multiple digits
        elif ch in OPS: 
            s.append(OPS[ch])
        elif ch == ')':
            b, op, a = s.pop(), s.pop(), s.pop() 
            s.append(op(a, b))
    return s.pop()
        

if __name__ == '__main__':
    cases = (
        ('(1 + 2)', 3),
        ('(1 - (1 - 1))', 1),
        ('((1 - 1) - 1)', -1),
        ('(1 - (1 - (1 - 1)))', 0),
        ('((1 + 2) - (3 + 4))', -4)
    )
    for expr, n in cases:
        res = calculate(expr)
        assert res == n, f'expected f("{expr}") to be {n}, got {res}'
    
    print('Tests passed')