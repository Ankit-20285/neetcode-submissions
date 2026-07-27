class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, open_count, close_count):

            # Base case
            if len(path) == 2 * n:
                ans.append(path)
                return

            # Add '(' if we still have some left
            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)

            # Add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans