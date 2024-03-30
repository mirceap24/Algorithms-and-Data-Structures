# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.

def wiggleSort(nums):
    # Sort array
    nums.sort()

    # Split array into two halves 
    half = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1 
    first_half = nums[:half]
    second_half = nums[half:]

    # Merge the two halves 
    nums.clear()
    for i in range(len(second_half)):
        if i < len(first_half):
            nums.append(first_half[i])
        if i < len(second_half):
            nums.append(second_half[i])
    
    return nums 

# Test 
print(wiggleSort([1,5,1,1,6,4]))
print(wiggleSort([1,3,2,2,3,1]))