class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = ""
        for letters in s.lower(): 
            if letters.isalnum(): 
                y += letters 

        for i in range(len(y)): 
            if y[i] != y[len(y) - i - 1]:
                return False
        
        return True