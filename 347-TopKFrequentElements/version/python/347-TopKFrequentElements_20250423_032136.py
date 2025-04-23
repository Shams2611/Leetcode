# Last updated: 4/23/2025, 3:21:36 AM
class Solution(object):
    def topKFrequent(self, nums, k):
        return [num for num, _ in Counter(nums).most_common(k)]
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        