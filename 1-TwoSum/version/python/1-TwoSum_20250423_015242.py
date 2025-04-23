# Last updated: 4/23/2025, 1:52:42 AM
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]

            num_map[num] = index

        return []

        