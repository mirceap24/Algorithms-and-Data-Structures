# https://leetcode.com/problems/reverse-bits/description/

def reverseBits(n):
    # Initialize result to 0
    result = 0
    
    # Loop through 32 times since we're dealing with a 32-bit integer
    for i in range(32):
        # Shift result to the left to make room for the next bit
        result <<= 1
        # Add the rightmost bit of n to result
        result |= n & 1
        # Shift n to the right to process the next bit
        n >>= 1
    
    # Return the reversed integer
    return result