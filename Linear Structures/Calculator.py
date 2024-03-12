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

class InvalidExpression(ValueError):
    pass 


def calculate(expr):
    s = []
    for ch in expr: 
        if ch.isdigit():
            if len(s) == 0 or not isinstance(s[-1], int):
                s.append(int(ch))
            else: 
                s[-1] = s[-1] * 10 + int(ch)
        elif ch in OPS: 
            s.append(OPS[ch])
        elif ch == ')':
            try:
                b, op, a = s.pop(), s.pop(), s.pop()
            except IndexError:
                raise InvalidExpression() 
            s.append(op(a, b))
    if len(s) != 1:
        raise InvalidExpression()
    return s.pop()
        

if __name__ == '__main__':
    cases = (
        ('(1 + 2)', 3),
        ('(1 - (1 - 1))', 1),
        ('((1 - 1) - 1)', -1),
        ('(1 - (1 - (1 - 1)))', 0),
        ('((1 + 2) - (3 + 4))', -4),
        ('(12 + 3)', 15),
        ('((12 + 3) + 12)', 27),
    )
    for expr, n in cases:
        res = calculate(expr)
        assert res == n, f'expected f("{expr}") to be {n}, got {res}'
    
    invalid = (
        '(1 + 2',
        '(1 +',
        '(1 + 2 + 3)',
    )

    for expr in invalid: 
        try: 
            calculate(expr)
        except InvalidExpression:
            continue 
        except Exception:
            pass
        raise AssertionError(f'expected {expr} to be detected as invalid')
    
    print('Tests passed')