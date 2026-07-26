class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list() 
        self.helper(nums, list(), 0, result)
        return result
        
    def helper(self, nums, so_far, i, result):
        result.append(list(so_far))
        for n in range(i, len(nums)):
            so_far.append(nums[n])
            self.helper(nums, so_far, n + 1, result)
            so_far.pop()
    