from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        char_tally = Counter("".join(words))
        pair_sum = 0
        single_sum = 0

        iter_values = list(char_tally.values())
        index_a = 0
        while index_a < len(iter_values):
            current_val = iter_values[index_a]
            div_val = current_val // 2
            mod_val = current_val - (div_val * 2)
            pair_sum += div_val
            single_sum += mod_val
            index_a += 1

        sorted_words = list(words)
        swapped = True
        while swapped:
            swapped = False
            idx_b = 0
            while idx_b < len(sorted_words) - 1:
                if len(sorted_words[idx_b]) > len(sorted_words[idx_b + 1]):
                    temp_word = sorted_words[idx_b]
                    sorted_words[idx_b] = sorted_words[idx_b + 1]
                    sorted_words[idx_b + 1] = temp_word
                    swapped = True
                idx_b += 1

        palindrome_count = 0
        idx_c = 0
        while True:
            if idx_c >= len(sorted_words):
                break
            current_word = sorted_words[idx_c]
            half_len = len(current_word) // 2
            if pair_sum >= half_len:
                pair_sum -= half_len
                palindrome_count += 1
            idx_c += 1

        return palindrome_count