# Divide and conquer approach to raise a number to the power of an integer n 

"""
exp(a, n) -> a * a * a * a * ... * a [n times]

exp(3, 8) -> 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 

3 ^ 8 = (3 ^ 4) ^ 2

"""

def exp(a, n):
    if n == 0:
        return 1 
    
    if n % 2 == 1: 
        return a * exp(a, n - 1)
    
    res = exp(a, n >> 1)
    return res * res

def exp_iter(a, n):
    res = 1 
    while n > 0:
        if n % 2 == 1: 
            res *= a 
            n -= 1 
        else: 
            a *= a 
            n >>= 1 
    return res

if __name__ == '__main__':
    assert exp(2, 5) == 32 
    assert exp(4, 4) == 256
    assert exp_iter(2, 5) == 32 
    assert exp_iter(4, 4) == 256
    print('Tests passed')