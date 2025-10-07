from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        count = 0
        seen = defaultdict(int)
        for word in reversed(words):
            for key in seen:
                if word == key[:len(word)] and word == key[-len(word):]:
                    count += seen[key]
            seen[word] += 1
        return count