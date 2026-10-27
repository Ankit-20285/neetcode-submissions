class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        Stack = [] 
        
        for i in range(len(temperatures)): 
            while Stack and temperatures[i] > temperatures[Stack[-1]]: 
                prev = Stack.pop() 
                res[prev] = i - prev 
            Stack.append(i)
        

        return res