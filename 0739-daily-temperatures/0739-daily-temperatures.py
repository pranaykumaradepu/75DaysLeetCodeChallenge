class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = [] 
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                past_day_index = stack.pop()
                days_waited = i - past_day_index
                res[past_day_index] = days_waited
            stack.append(i)
        return res