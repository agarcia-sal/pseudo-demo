from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        total_length = len(word)
        partition_list = []
        pointer = 0
        while pointer < total_length:
            segment_end = pointer + k
            partition_list.append(word[pointer:segment_end])
            pointer += k

        frequency_map = Counter(partition_list)
        highest_frequency = max(frequency_map.values())
        difference = len(partition_list) - highest_frequency
        return difference