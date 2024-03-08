# At what point is binary search substantially better than linear search? 

from random import randint 
import timeit
from matplotlib import pyplot

def binsearch(nums, n):
    lo, hi = 0, len(nums)
    while hi > lo: 
        mid = (lo + hi) // 2 
        x = nums[mid]
        if x == n: 
            return mid 
        if n < x: 
            hi = mid 
        if n > x: 
            lo = mid + 1 
    return None 

def itersearch(nums, n):
    for i, x in enumerate(nums):
        if n == x: 
            return i 
    return None

if __name__ == '__main__':
   sizes = range(200)
   bintiming, itertiming = [], []
   for size in sizes: 
       nums = sorted(randint(0, 10000) for _ in range(size))
       bintiming.append(timeit.timeit(lambda: binsearch(nums, 42), number = 3))
       itertiming.append(timeit.timeit(lambda: itersearch(nums, 42), number = 3))

   pyplot.plot(sizes, bintiming, itertiming)
   pyplot.show()
   