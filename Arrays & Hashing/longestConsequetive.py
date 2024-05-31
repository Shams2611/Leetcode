class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                current = n
                length = 1

                while (current + 1) in numSet:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
        
        return longest
