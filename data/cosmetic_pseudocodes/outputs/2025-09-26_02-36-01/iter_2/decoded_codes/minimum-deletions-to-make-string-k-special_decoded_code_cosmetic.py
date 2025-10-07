class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        char_counts = {}
        for char in word:
            char_counts[char] = char_counts.get(char, 0) + 1

        freq_list = sorted(char_counts.values())  # ascending order

        best_deletions = float('inf')
        idx = 0
        n = len(freq_list)
        while idx < n:
            max_freq_allowed = freq_list[idx] + k

            deletions_count = 0
            for j in range(idx + 1, n):
                current_freq = freq_list[j]
                if current_freq > max_freq_allowed:
                    deletions_count += current_freq - max_freq_allowed

            for m in range(idx):
                deletions_count += freq_list[m]

            if deletions_count < best_deletions:
                best_deletions = deletions_count

            idx += 1

        return best_deletions