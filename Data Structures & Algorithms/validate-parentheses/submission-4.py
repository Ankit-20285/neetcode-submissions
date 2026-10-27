class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []

        for i in s: 
            if i == "(" or i == "{" or i == "[": 
                Stack.append(i)
            else: 
                if not Stack: 
                    return False
                if i == ")" and Stack[-1] == "(": 
                    Stack.pop()
                elif i == "}" and Stack[-1] == "{":
                    Stack.pop()
                elif i == "]" and Stack[-1] == "[": 
                    Stack.pop()
                else: 
                    return False
        
        return len(Stack) == 0
