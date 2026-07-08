class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # Build frequency maps
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        for ch in s2[:len(s1)]:
            window_count[ch] = window_count.get(ch, 0) + 1

        if s1_count == window_count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            # Add new character
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # Remove old character
            window_count[s2[left]] -= 1

            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1

            if window_count == s1_count:
                return True

        return False