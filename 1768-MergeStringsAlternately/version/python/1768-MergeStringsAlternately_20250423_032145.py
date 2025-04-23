# Last updated: 4/23/2025, 3:21:45 AM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0
        res = []
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
                i += 1
            if j < len(word2):
                res.append(word2[j])
                j += 1
        return "".join(res)








        