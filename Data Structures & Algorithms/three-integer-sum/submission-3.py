class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        result = list()
        for num in range(len(new_nums) - 2):
            left = num
            for right in range(left + 1, len(new_nums)):
                if -1 * (new_nums[left] + new_nums[right]) in new_nums[right + 1:len(new_nums)]:
                    if [new_nums[left], new_nums[right], new_nums[new_nums.index(-1 * (new_nums[left] + new_nums[right]))]] not in result:
                        result.append([new_nums[left], new_nums[right], new_nums[new_nums.index(-1 * (new_nums[left] + new_nums[right]))]])
        return result