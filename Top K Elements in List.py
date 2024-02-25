# Question: https://neetcode.io/problems/top-k-elements-in-list

# My initial bruteforce attempt to sort the list and accessing the last element 
#this just returns the last element of the sorted list 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution_arr = []
        nums.sort()
        solution_arr.append(nums[len(nums) - 1])
        return solution_arr
    

