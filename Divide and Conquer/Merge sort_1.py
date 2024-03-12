"""
1. Basic mergesort with slicing/copying as needed 

"""

def merge(xs, ys):
    res = []
    xi, yi = 0, 0 
    while True:
        if xi == len(xs):
            return res + ys[yi:]
        if yi == len(ys):
            return res + xs[xi:]
        x, y = xs[xi], ys[yi]
        if x < y: 
            res.append(x)
            xi += 1 
        else:
            res.append(y)
            yi += 1
    

def mergesort(nums):
    # an array of 0 or 1 element is already sorted 
    if len(nums) <= 1: 
        return nums 
    
    mid = len(nums) // 2 
    return merge(mergesort(nums[:mid]), mergesort(nums[mid:]))


if __name__ == '__main__':
    nums = [4, 8, 2, 1, 3, 7, 2, -1, 5]
    expected = sorted(nums)
    actual = mergesort(nums)
    assert actual == expected, actual
    print('Test passed')