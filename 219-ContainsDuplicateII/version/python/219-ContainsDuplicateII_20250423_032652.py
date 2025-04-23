# Last updated: 4/23/2025, 3:26:52 AM
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        for i, x in enumerate(nums):
            if x in last_seen and i - last_seen[x] <= k:
                return True
            last_seen[x] = i
        return False