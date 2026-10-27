class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        Stack = []

        for i in range(n): 
            while Stack and temperatures[i] > temperatures[Stack[-1]]: 
                prev = Stack.pop() 
                ans[prev] = i - prev 
            Stack.append(i)
    
        return ans