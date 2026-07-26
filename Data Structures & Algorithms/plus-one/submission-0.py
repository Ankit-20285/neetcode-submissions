class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate through the array in reverse order
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        # If all digits were 9, we need an extra leading 1 (e.g., [9, 9] -> [1, 0, 0])
        return [1] + digits