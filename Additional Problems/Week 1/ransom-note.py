# https://leetcode.com/problems/ransom-note/description/

def canConstruct(ransomNote, magazine):
    # dictionary for the letter counts of the magazine 
    magazine_counts = {}

    for char in magazine: 
        if char in magazine_counts:
            magazine_counts[char] += 1 
        else:
            magazine_counts[char] = 1

    
    # Go through the ransom note and decrease the count of each letter 
    for char in ransomNote: 
        if char not in magazine_counts or magazine_counts[char] == 0: 
            return False 
        magazine_counts[char] -= 1 
    
    return True 