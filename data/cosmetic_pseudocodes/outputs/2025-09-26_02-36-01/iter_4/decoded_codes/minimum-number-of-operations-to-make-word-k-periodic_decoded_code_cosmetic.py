from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        length_of_word = len(word)
        parts = []
        current_index = 0
        while current_index <= length_of_word - k:
            segment = word[current_index:current_index + k]
            parts.append(segment)
            current_index += k

        frequency_map = Counter(parts)
        highest_frequency = max(frequency_map.values(), default=0)
        operations_needed = len(parts) - highest_frequency
        return operations_needed