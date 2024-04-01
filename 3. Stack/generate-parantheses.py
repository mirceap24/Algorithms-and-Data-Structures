"""
Problem: LeetCode 22 - Generate Parentheses

Key Idea:
To generate all valid combinations of parentheses, we can use backtracking. We start with an empty string and two counters, one for the open parentheses and one for the close parentheses. At each step, we have two choices: add an open parenthesis if the count of open parentheses is less than the total number of pairs, or add a close parenthesis if the count of close parentheses is less than the count of open parentheses. We continue this process recursively until we reach the desired length of the string. If the string becomes valid, we add it to the result.

Time Complexity:
The time complexity of this solution is O(4^n / sqrt(n)), where n is the number of pairs of parentheses. This is because each valid combination is a sequence of open and close parentheses of length 2n, and there are 2^(2n) such sequences. However, not all sequences are valid, and the Catalan number (4^n / sqrt(n)) bounds the number of valid combinations.

Space Complexity:
The space complexity is O(4^n / sqrt(n)) as well, as this is the maximum number of valid combinations that can be generated.
"""

class Solution: 
    def generateParantheses(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n: 
                res.append("".join(stack))
            
            if openN < closedN: 
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN: 
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
    
        backtrack(0, 0)
        return res