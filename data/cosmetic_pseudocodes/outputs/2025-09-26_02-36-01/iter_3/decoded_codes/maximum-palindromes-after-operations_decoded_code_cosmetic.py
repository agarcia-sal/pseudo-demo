class Solution:
    def maxPalindromesAfterOperations(self, words):
        freq_map = {}
        for current_str in words:
            for c in current_str:
                freq_map[c] = freq_map.get(c, 0) + 1

        total_pairs = 0
        total_singles = 0
        for cnt in freq_map.values():
            pairs_from_cnt = (cnt - (cnt % 2)) // 2
            total_pairs += pairs_from_cnt
            total_singles += (cnt & 1)

        ordered_words = sorted(words, key=len)

        palindrome_count = 0
        for w in ordered_words:
            half_len = len(w) // 2
            if total_pairs >= half_len:
                total_pairs -= half_len
                palindrome_count += 1

        return palindrome_count