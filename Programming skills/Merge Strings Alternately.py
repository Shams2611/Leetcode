class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_word = []
        length1 = len(word1)
        length2 = len(word2)
        max_length = max(len(word1), len(word2))

        for i in range(max_length):
            if i < length1:
                new_word.append(word1[i])
            if i < length2:
                new_word.append(word2[i])

        return ''.join(new_word)