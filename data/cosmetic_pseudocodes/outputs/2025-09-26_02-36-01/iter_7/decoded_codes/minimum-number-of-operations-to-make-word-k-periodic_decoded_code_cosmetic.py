class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        total_length = len(word)
        fragment_list = []
        pos = 0
        while pos < total_length:
            block = word[pos:pos + k]
            fragment_list.append(block)
            pos += k

        frequency_map = {}
        for element in fragment_list:
            frequency_map[element] = frequency_map.get(element, 0) + 1

        maximum_frequency = 0
        for key in frequency_map:
            if frequency_map[key] > maximum_frequency:
                maximum_frequency = frequency_map[key]

        total_fragments = len(fragment_list)
        answer = total_fragments - maximum_frequency
        return answer