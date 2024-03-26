# https://leetcode.com/problems/counting-bits/description/

# number of bits in i is 1 + the number of bits in i with last set bit removed 
# i & (i - 1)

def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1 
    return ans
