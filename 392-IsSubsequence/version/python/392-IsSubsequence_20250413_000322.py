# Last updated: 4/13/2025, 12:03:22 AM
class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        n, m = len(s), len(t)
        if n == 0:
            return True
        while j < m:
            if s[i] == t[j]:
                i += 1
                if i == n:
                    return True
            j += 1
        return False