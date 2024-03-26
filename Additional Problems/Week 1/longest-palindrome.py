from collections import Counter 

def longestPalindrome(s):
    counts = Counter(s)
    length = 0 

    odd_occurence = False 

    for count in counts.values():
        # if count is even, it can fully contribute to the palindrome 
        if count % 2 == 0: 
            length += count 
        else: 
            # if the count is odd, we can use the even part of it 
            length += count - 1 
            odd_occurence = True 
    
    # if there's at least one character with an odd occurence,
    # we can put it in the middle of the palindrome 
    if odd_occurence: 
        length += 1 
    
    return length 