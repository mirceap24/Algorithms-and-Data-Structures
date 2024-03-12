"""
Refactor steps: 
- do in place 
- do without slicing 
"""

def mergesort(nums):
    working = [0] * len(nums)

    def merge(left, right, mid):
        for i in range(left, right):
            working[i] = nums[i]
        
        li, ri = left, mid 
        for i in range(left, right):
            if ri == right or ((li != mid) and working[li] < working[ri]):
                nums[i] = working[li]
                li += 1 
            else: 
                nums[i] = working[ri]
                ri += 1 
    
    def sort(left, right):
        """
        Sort the range in nums defined by [left, right)
        """
        if right - left <= 1: 
            return 
        mid = (right + left) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, right, mid)
    
    sort(0, len(nums))

if __name__ == '__main__':
    nums = [4, 8, 2, 1, 3, 7, 2, -1, 5]
    expected = sorted(nums)
    mergesort(nums)
    assert nums == expected, nums 
    print('Test passed')
