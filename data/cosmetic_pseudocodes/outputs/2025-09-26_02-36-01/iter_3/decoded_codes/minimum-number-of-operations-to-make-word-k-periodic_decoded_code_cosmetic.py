class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        total_length = len(word)
        slices = []
        start_pos = 0
        while start_pos < total_length:
            end_pos = start_pos + k
            current_slice = word[start_pos:end_pos]
            slices.append(current_slice)
            start_pos += k

        frequency_map = {}
        for segment in slices:
            frequency_map[segment] = frequency_map.get(segment, 0) + 1

        highest_freq = 0
        for count in frequency_map.values():
            if count > highest_freq:
                highest_freq = count

        output_value = len(slices) - highest_freq
        return output_value