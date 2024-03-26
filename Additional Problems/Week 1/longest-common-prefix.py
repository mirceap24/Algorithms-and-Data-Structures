# https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    # if the list is empty, return empty string 
    if not strs: 
        return ""
    
    # initialize the prefix with first string
    prefix = strs[0]

    # traverse through each string in the array starting from the second one
    for s in strs[1:]:
        # compare string with current prefix 
        while not s.starswith(prefix):
            # truncate last char from prefix 
            prefix = prefix[:-1]
            if not prefix: 
                return ""
    
    return prefix 

