class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.recur(nums, 0, [], result)
        return result

    def recur(self, nums, start, so_far, res):
        res.append(so_far[:])

        for n in range(start, len(nums)):
            so_far.append(nums[n])
            self.recur(nums, n + 1, so_far, res)
            so_far.pop()