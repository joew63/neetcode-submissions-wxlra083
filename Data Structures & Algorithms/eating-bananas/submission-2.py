from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            # Hours needed to eat all piles at rate `mid`
            hours_needed = sum(ceil(p / mid) for p in piles)

            if hours_needed <= h:
                hi = mid      # mid might be the answer, but try smaller
            else:
                lo = mid + 1  # too slow, need higher rate

        return lo