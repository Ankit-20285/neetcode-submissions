
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        while L <= R:
            mid = (L + R) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                R = mid - 1
            else:
                L = mid + 1

        return L
