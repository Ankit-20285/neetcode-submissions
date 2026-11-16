class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            max_val = -1
            for j in range(i + 1, len(arr)):
                max_val = max(max_val, arr[j])
            arr[i] = max_val

        arr[-1] = -1
        return arr