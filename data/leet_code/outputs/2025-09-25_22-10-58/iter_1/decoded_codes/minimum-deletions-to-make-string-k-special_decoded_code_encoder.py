from collections import Counter
from math import inf

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        frequency_map = Counter(word)
        frequency_values = sorted(frequency_map.values())
        minimum_deletions = inf

        for index in range(len(frequency_values)):
            max_allowed_frequency = frequency_values[index] + k
            deletions = 0

            # Delete excess from frequencies greater than max_allowed_frequency after current index
            for freq in frequency_values[index + 1:]:
                if freq > max_allowed_frequency:
                    deletions += freq - max_allowed_frequency

            # Delete all frequencies before current index
            deletions += sum(frequency_values[:index])

            if deletions < minimum_deletions:
                minimum_deletions = deletions

        return minimum_deletions