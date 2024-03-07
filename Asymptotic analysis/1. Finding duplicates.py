# Given an array of integers, write a function that returns if all 
# elements are unique 

# Option 1: for each n in array, check every m in array for equality => O(n^2) time complexity, O(1) space complexity

# Option 2: sort the array, iterate through checking adjacent pairs
    ## O(n * logn) to sort + O(n) to iterate => O(n * logn) time complexity 
    ## O(n) space complexity, but there are in-memory sort algorithms

# Option 3: iterate once through, building a hashmap as we go
    ## Lookup in hashmap is constant time, O(1)
    ## Still need to iterate through the array => O(n) time complexity, O(n) space complexity 



