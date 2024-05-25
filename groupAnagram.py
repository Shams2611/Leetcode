# Question: https://neetcode.io/problems/anagram-groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMaps = defaultdict(list)
        for index, word in enumerate(strs):
            hashMaps[tuple(sorted(word))].append(word)
        return hashMaps.values()