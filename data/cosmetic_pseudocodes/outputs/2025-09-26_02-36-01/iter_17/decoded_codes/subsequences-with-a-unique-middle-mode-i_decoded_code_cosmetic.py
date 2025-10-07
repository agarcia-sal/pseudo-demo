from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        CONST_MODULO = 10**9 + 7
        size_nums = len(nums)
        if size_nums < 5:
            return 0

        comb_set = self.generate_combinations(nums, 5)
        total_count = 0

        comb_index = 0
        while comb_index < len(comb_set):
            current_subseq = comb_set[comb_index]
            frequency_map = self.map_frequencies(current_subseq)
            median_element = current_subseq[2]
            median_freq = frequency_map[median_element]

            verify_unique = True
            freq_keys = list(frequency_map.keys())
            key_pos = 0

            while True:
                if key_pos >= len(freq_keys):
                    break
                current_key = freq_keys[key_pos]
                current_freq = frequency_map[current_key]
                if (current_key != median_element) and (current_freq >= median_freq):
                    verify_unique = False
                    break
                key_pos += 1

            if verify_unique:
                total_count += 1
            comb_index += 1

        return total_count % CONST_MODULO

    def generate_combinations(self, collection, select_count):
        result = []
        def helper(index, chosen):
            if len(chosen) == select_count:
                result.append(chosen[:])
                return
            if index >= len(collection):
                return
            helper(index + 1, chosen)
            chosen.append(collection[index])
            helper(index + 1, chosen)
            chosen.pop()
        helper(0, [])
        return result

    def map_frequencies(self, array):
        freq_map = {}
        pos = 0
        while True:
            if pos >= len(array):
                break
            element = array[pos]
            if element not in freq_map:
                freq_map[element] = 1
            else:
                freq_map[element] += 1
            pos += 1
        return freq_map