# Question: https://neetcode.io/problems/anagram-groups
# My solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMaps = defaultdict(list)
        for index, word in enumerate(strs):
            hashMaps[tuple(sorted(word))].append(word)
        return hashMaps.values()
    
#Neetcode solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()