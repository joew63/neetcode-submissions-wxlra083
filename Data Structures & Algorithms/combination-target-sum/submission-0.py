class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        self.check(nums, target, 0, 0, list(), result)
        return result

    def check(self, nums, target, count, index, current, result):
        if target == count:
            result.append(list(current))
            return
        if count < target:
            for i in range(index, len(nums)):
                current.append(nums[i])
                self.check(nums, target, count + nums[i], i, current, result)
                current.pop()
        return