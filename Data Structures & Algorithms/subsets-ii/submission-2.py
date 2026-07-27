class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = list() 
        nums.sort()
        self.helper(nums, list(), 0, result)
        return result
        
    def helper(self, nums, so_far, i, result):
        result.append(list(so_far))
        for n in range(i, len(nums)):
            if n > i and nums[n] == nums[n - 1]:
                continue
            so_far.append(nums[n])
            self.helper(nums, so_far, n + 1, result)
            so_far.pop()
    