class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1

        for i in range(len(arr) - 1, -1, -1):
            max_val, arr[i] = max(max_val, arr[i]), max_val

        return arr