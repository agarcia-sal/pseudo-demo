from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        character_count = Counter(''.join(words))
        pairs = 0
        singles = 0
        for count in character_count.values():
            pairs += count // 2
            singles += count % 2
        words.sort(key=len)
        palindromes = 0
        for word in words:
            half_length = len(word) // 2
            if pairs >= half_length:
                pairs -= half_length
                palindromes += 1
        return palindromes