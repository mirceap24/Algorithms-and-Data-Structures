# https://leetcode.com/problems/missing-number/description/

def missingNumber(nums):
    # calculate expected sum of numbers from 0 to n
    n = len(nums)
    expected_sum = n * (n + 1) // 2 

    actual_sum = sum(nums)

    return expected_sum - actual_sum

