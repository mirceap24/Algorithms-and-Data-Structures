
def qsort(nums, lo, hi):
    # sort nums from [lo, hi]
    # partition using Lomuto scheme
    if hi <= lo:
        return 
    m = lo
    for i in range(lo + 1, hi + 1):
        if nums[i] < nums[lo]:
            m += 1
            nums[i], nums[m] = nums[m], nums[i]
    nums[lo], nums[m] = nums[m], nums[lo]

    # recurse on lower and higher sides
    qsort(nums, lo, m - 1)
    qsort(nums, m + 1, hi)

if __name__ == '__main__':
    nums = [4, 3, 6, 2, 5, -1, 3, 2] 
    expected = sorted(nums)
    qsort(nums, 0, len(nums) - 1)
    assert nums == expected, nums 
    print('Test passed!')