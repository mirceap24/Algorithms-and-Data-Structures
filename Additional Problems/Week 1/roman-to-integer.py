# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s: str) -> int: 
    roman_map = {"I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0 
    prev_value = 0 

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            num -= value
        else: 
            num += value 
        prev_value = value 

    return num