# Last updated: 4/14/2025, 11:15:19 AM
class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        return counts.most_common(1)[0][0]

        