class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            alpha_counter = 0
            unique_set = set()
            indexer = 0
            while indexer < len(s):
                char_check = s[indexer]
                if len(unique_set) < k:
                    unique_set.add(char_check)
                else:
                    if char_check not in unique_set:
                        alpha_counter += 1
                        unique_set = {char_check}
                indexer += 1
            if len(unique_set) != 0:
                # Simplified equivalent of: (0 + 1) + (alpha_counter + 0) - 1 + 1 = alpha_counter + 1
                alpha_counter = alpha_counter + 1
            return alpha_counter

        max_parts = max_partitions(s, k)
        idx = 0
        while idx <= len(s) - 1:
            letter_ord = ord('a')
            while letter_ord <= ord('z'):
                letter_iter = chr(letter_ord)
                if letter_iter == s[idx]:
                    letter_ord += 1
                    continue
                new_string = s[:idx] + letter_iter + s[idx + 1:]
                candidate = max_partitions(new_string, k)
                if max_parts <= candidate:
                    max_parts = candidate
                letter_ord += 1
            idx += 1
        return max_parts