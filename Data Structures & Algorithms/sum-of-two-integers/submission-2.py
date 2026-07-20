class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to simulate 32-bit integer behavior
        mask = 0xFFFFFFFF
        
        while b != 0:
            # Calculate the carry, but keep it within 32 bits
            carry = (a & b) << 1
            # Add without carry
            a = (a ^ b) & mask
            # Shift the carry to b, also keeping it within 32 bits
            b = carry & mask
        
        # If the 32nd bit is 1, it means the number is negative in 32-bit signed terms
        # We need to convert it back to Python's representation of a negative number
        if a > 0x7FFFFFFF:
            return ~(a ^ mask)
        
        return a