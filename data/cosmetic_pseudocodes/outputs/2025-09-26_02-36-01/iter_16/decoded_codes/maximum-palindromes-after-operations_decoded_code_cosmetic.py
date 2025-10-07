class Solution:
    def maxPalindromesAfterOperations(self, words):
        # Count character frequencies across all words
        char_count = {}
        for word in words:
            for ch in word:
                char_count[ch] = char_count.get(ch, 0) + 1

        pairs_total = 0
        singles_total = 0
        for count in char_count.values():
            pairs_contrib = (count - (count % 2)) // 2
            singles_contrib = count % 2
            pairs_total += pairs_contrib
            singles_total += singles_contrib

        # Sort words by length using insertion sort as in pseudocode
        sorted_words = words[:]  # copy to avoid modifying input
        for i in range(1, len(sorted_words)):
            key_word = sorted_words[i]
            j = i - 1
            while j >= 0 and len(sorted_words[j]) > len(key_word):
                sorted_words[j + 1] = sorted_words[j]
                j -= 1
            sorted_words[j + 1] = key_word

        result = 0
        for word in sorted_words:
            pairs_needed = (len(word) - (len(word) % 2)) // 2
            if pairs_total - pairs_needed >= 0:
                pairs_total -= pairs_needed
                result += 1

        return result