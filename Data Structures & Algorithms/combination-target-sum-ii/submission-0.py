class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(index, path, targetSum):
            if targetSum == 0: 
                res.append(path.copy())
                return 
            
            if targetSum < 0: 
                return 

            for i in range(index, len(candidates)): 
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                diff = targetSum - candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, path, diff)
                path.pop()
        
        backtrack(0, [], target)
        return res
