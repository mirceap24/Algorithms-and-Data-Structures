# https://leetcode.com/problems/climbing-stairs/description/

def climbStairs(n):
    if n == 1: 
        return 1 
    if n == 2: 
        return 2 
    
    one_step_before = 2 
    two_steps_before = 1

    # start at step 3 and build up to n 
    all_ways = 0 
    for i in range(3, n + 1):
        # The number of ways to get to this step is the sum of the ways
        # to get to the one step before and two steps before this one
        all_ways = one_step_before + two_steps_before

        # update steps for next iteration 
        two_steps_before = one_step_before
        one_step_before = all_ways
    
    return all_ways
