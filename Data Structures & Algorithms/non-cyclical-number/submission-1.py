class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4: 
            sum = 0 
            while n > 0: 
                rem = n%10 
                sum += rem*rem 
                n = int(n / 10)
            
            n = sum 

        if n == 1: 
            return True 
        else: 
            return False
        

        