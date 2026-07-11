class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []

        for i in s: 
            if i == "(" or i == "{" or i == "[":
                myStack.append(i)
            
            else: 
                if len(myStack) == 0: 
                    return False
                
                if i == ")" and myStack[-1] == "(": 
                    myStack.pop()
                elif i == "}" and myStack[-1] == "{": 
                    myStack.pop()
                elif i == "]" and myStack[-1] == "[": 
                    myStack.pop()
                else: 
                    return False
                
        return not myStack