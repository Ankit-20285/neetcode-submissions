class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # Dictionary to store the target frequency of characters in t
        target_counts = Counter(t)
        required = len(target_counts) # Number of unique characters needed
        
        # Dictionary to store the current window's character frequencies
        window_counts = {}
        
        # formed tracks how many unique characters meet their target count in the window
        formed = 0
        
        # Left and right pointers for the window
        left, right = 0, 0
        
        # Tuple to track the result: (window_length, left_idx, right_idx)
        min_len_info = (float('inf'), None, None)
        
        while right < len(s):
            # Expand the window by adding the character at the right pointer
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If this character's count matches its target count in t, increment formed
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
                
            # Contract the window from the left once a valid window is found
            while left <= right and formed == required:
                char_left = s[left]
                
                # Save the smallest valid window found so far
                current_len = right - left + 1
                if current_len < min_len_info[0]:
                    min_len_info = (current_len, left, right)
                
                # Shrink the window from the left
                window_counts[char_left] -= 1
                if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                    formed -= 1
                
                left += 1
                
            # Keep expanding the window to the right
            right += 1
            
        # Return the minimum window substring if found, otherwise return empty string
        length, l_idx, r_idx = min_len_info
        return s[l_idx : r_idx + 1] if length != float('inf') else ""