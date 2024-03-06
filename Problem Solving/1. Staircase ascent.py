# Staircase of n steps and my legs are long enough that I could
# go up 1, 2 or 3 steps. How many different ways can I go up the staircase? 

def f(n): 
    if n <= 2: 
        return (1, 1, 2)[n]
    return f(n - 1) + f(n - 2) + f(n - 3)

def f2(n):
    a, b, c = 1, 1, 2 
    for _ in range(n):
        a, b, c = b, c, a + b + c 
    return a

if __name__ == '__main__':
    expectations = (1, 1, 2, 4, 7, 13)
    for i, x in enumerate(expectations):
        assert f(i) == x
        assert f2(i) == x 
    print('Tests passed') 