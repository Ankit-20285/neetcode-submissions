class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num = bin(n)[2:]
        binary_num = binary_num.zfill(32)
        binary_num = binary_num[::-1]
        number = int(binary_num, 2)

        return number