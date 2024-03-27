# https://leetcode.com/problems/move-zeroes/description/

def moveZeroes(nums):
    non_zero_index = 0 

    # place all non-zero elements at the beginning of the array 
    for i in range(len(nums)):
        if nums[i] != 0: 
            # swap current element with the element at non-zero index 
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            # move the non_zero_index forward 
            non_zero_index += 1