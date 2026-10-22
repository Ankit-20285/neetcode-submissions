class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        a = s[::-1]

        if s == a: 
            return True 
        else: 
            return False
        
        
