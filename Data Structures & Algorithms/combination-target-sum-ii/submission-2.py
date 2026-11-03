class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(start, path, target):
            if target == 0:
                ans.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]: 
                    continue
                remain = target - candidates[i]
                if remain < 0:
                    break  # sorted, so everything after overshoots too
                path.append(candidates[i])
                backtrack(i + 1, path, remain)
                path.pop()


        backtrack(0, [], target)
        return ans