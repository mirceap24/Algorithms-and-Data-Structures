# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n 
        while left < right: 
            mid = left + (right - left) // 2 
            if isBadVersion(mid):
                right = mid # The first bad version is in the left half
            else: 
                left = mid + 1 # The first bad version is in the right half
        
        return left  # At this point, left == right, pointing to the first bad version