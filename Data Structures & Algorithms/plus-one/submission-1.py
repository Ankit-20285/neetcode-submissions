class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digs = 0 

        for digit in digits: 
            digs = (digs * 10) + digit 
        
        digs += 1 
        
        li = [int(digit) for digit in str(digs)]

        return li