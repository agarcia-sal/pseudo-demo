from math import inf

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq_map = {}
        idx = 0
        while idx < len(word):
            ch = word[idx]
            if ch in freq_map:
                freq_map[ch] += 1
            else:
                freq_map[ch] = 1
            idx += 1

        freq_list = list(freq_map.values())

        # Sort freq_list in ascending order using built-in sort for efficiency
        freq_list.sort()

        min_deletions = inf
        last_index = len(freq_list) - 1

        def dfs(i):
            nonlocal min_deletions
            if i > last_index:
                return

            threshold = freq_list[i] + k
            deletions = 0

            # Count deletions for frequencies greater than threshold
            for j in range(i + 1, last_index + 1):
                if freq_list[j] > threshold:
                    deletions += freq_list[j] - threshold

            # Add frequencies less than current index (all removed)
            for j in range(i):
                deletions += freq_list[j]

            if deletions < min_deletions:
                min_deletions = deletions

            dfs(i + 1)

        dfs(0)
        return min_deletions