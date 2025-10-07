from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        freq_map = Counter()
        for word in words:
            for char in word:
                freq_map[char] += 1

        total_pairs = 0
        total_singles = 0
        for count in freq_map.values():
            total_pairs += count // 2
            total_singles += count % 2

        words.sort(key=len)

        palindrome_count = 0
        for word in words:
            half_len = len(word) // 2
            if total_pairs >= half_len:
                total_pairs -= half_len
                palindrome_count += 1

        return palindrome_count