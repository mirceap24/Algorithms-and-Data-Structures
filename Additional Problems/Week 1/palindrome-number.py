# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x):
    # negative numbers are not palindrome 
    # if the last digit is 0, it can only be palindrome if the number is 0 
    if x < 0 or (x % 10 == 0 and x != 0):
        return False 
    
    # rever half of the number
    reverted_number = 0
    while x > reverted_number: 
        reverted_number = reverted_number * 10 + x % 10
        x //= 10
    
    # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10.
    # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    # since the middle digit doesn't matter in palindrome (it will always equal to itself),
    # we can simply get rid of it.
    return x == reverted_number or x == reverted_number // 10
    