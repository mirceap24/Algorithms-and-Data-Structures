# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead

class Solution:
    def dailyTemperatures(self, temperatures):

        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append([t, i])
        
        return result
    

sol = Solution()

temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
assert sol.dailyTemperatures(temperatures1) == [1, 1, 4, 2, 1, 1, 0, 0]
print('Test passed')