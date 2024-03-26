# https://leetcode.com/problems/single-number/description/

def singleNumber(nums):
    single = 0 

    for num in nums: 
        # num xor num = 0 
        # num xor 0 = num
        single ^= num 
    
    return single 