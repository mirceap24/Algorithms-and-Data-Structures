# https://leetcode.com/problems/backspace-string-compare/description/

def backspaceCompare(S: str, T: str) -> bool: 
    def build(string):
        result = []
        skip = 0 
        for char in reversed(string):
            if char == '#':
                skip += 1 
            elif skip: 
                skip -= 1 
            else: 
                result.append(char)
        
        return ''.join(result)