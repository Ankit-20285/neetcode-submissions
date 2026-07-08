class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter '#' to get the end of the length prefix
            while s[j] != '#':
                j += 1
            
            # Extract the length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            # The string starts right after '#' (at j + 1)
            start_idx = j + 1
            end_idx = start_idx + length
            res.append(s[start_idx:end_idx])
            
            # Move the pointer to the start of the next encoded block
            i = end_idx
            
        return res