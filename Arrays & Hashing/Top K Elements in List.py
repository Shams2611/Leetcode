# Question: https://neetcode.io/problems/top-k-elements-in-list

# My initial bruteforce attempt to sort the list and accessing the last element 
#this just returns the last element of the sorted list 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution_arr = []
        nums.sort()
        solution_arr.append(nums[len(nums) - 1])
        return solution_arr
    

#Neetcode solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res