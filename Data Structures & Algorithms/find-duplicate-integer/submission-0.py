class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        so_far = set()
        for n in nums:
            if n in so_far:
                return n
            so_far.add(n)
        return None