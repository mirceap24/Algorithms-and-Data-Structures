# https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sortedSquares(nums):
    # Initialize an array of the same length as nums, filled with zeros.
    result = [0] * len(nums)

    # two pointers technique 
    left, right = 0, len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left] > abs(nums[right])):
            # square left element and move the left pointer 
            result[i] = nums[left] ** 2 
            left += 1 
        else: 
            result[i] = nums[right] ** 2
            right -= 1 
    
    return result 