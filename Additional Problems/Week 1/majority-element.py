# https://leetcode.com/problems/majority-element/description/

def majorityElement(nums):
    candidate = None 
    count = 0 

    for num in nums: 
        if count == 0:
            # if count is zero, we choose the current number as candidate
            candidate = num 
        # if the current number is the candidate, increase the count 
        # else decrease it 
        count += (1 if num == candidate else - 1)
    
    return candidate
        
