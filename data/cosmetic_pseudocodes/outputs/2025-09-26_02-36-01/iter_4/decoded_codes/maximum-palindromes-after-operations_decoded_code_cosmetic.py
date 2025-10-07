class Solution:
    def maxPalindromesAfterOperations(self, words):
        glyph_frequencies = {}
        concatenated_string = "".join(words)
        for ch in concatenated_string:
            glyph_frequencies[ch] = glyph_frequencies.get(ch, 0) + 1

        total_pairs = 0
        total_singles = 0
        frequency_iterator = list(glyph_frequencies.values())
        current_index = 0
        while current_index < len(frequency_iterator):
            freq_value = frequency_iterator[current_index]
            total_pairs += freq_value // 2
            modulo_value = freq_value - (freq_value // 2) * 2
            total_singles += modulo_value
            current_index += 1

        sorted_words = sorted(words, key=len)
        palindrome_count = 0
        word_index = 0
        total_words = len(sorted_words)
        while word_index < total_words:
            current_word = sorted_words[word_index]
            half_len = len(current_word) // 2
            if not (total_pairs < half_len):
                total_pairs -= half_len
                palindrome_count += 1
            word_index += 1

        return palindrome_count