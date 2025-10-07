from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        total_length = len(word)
        segment_list = []
        iterator_index = 0

        while iterator_index < total_length:
            end_index = iterator_index + k
            current_piece = word[iterator_index:end_index]
            segment_list.append(current_piece)
            iterator_index += k

        frequency_map = Counter(segment_list)
        highest_frequency = max(frequency_map.values()) if frequency_map else 0
        final_result = len(segment_list) - highest_frequency

        return final_result