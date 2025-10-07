from math import inf
from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        char_counts = Counter(word)
        freq_list = sorted(char_counts.values())

        best_result = inf
        length = len(freq_list)

        for iter in range(length):
            max_freq_boundary = freq_list[iter] + k
            total_deletions = 0

            # Count deletions needed for frequencies greater than max_freq_boundary
            for pos in range(iter + 1, length):
                if freq_list[pos] > max_freq_boundary:
                    total_deletions += freq_list[pos] - max_freq_boundary

            # Add all frequencies less than current iter (they must be fully deleted)
            for rev_pos in range(iter):
                total_deletions += freq_list[rev_pos]

            if total_deletions < best_result:
                best_result = total_deletions

        return best_result