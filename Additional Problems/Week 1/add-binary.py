# https://leetcode.com/problems/add-binary/description/

def addBinary(a, b):
    result = []
    carry = 0 
    i, j = len(a) - 1, len(b) - 1 

    # iterate over both strings from right to left 
    while i >= 0 or j >= 0: 
        sum = carry 
        if i >= 0: 
            sum += int(a[i])
            i -= 1 
        if j >= 0: 
            sum += int(b[j])
            j -= 1 
        
        result.append(str(sum % 2))

        carry = sum // 2 

    if carry: 
        result.append('1')
        
    return ''.join(result[::-1])
    