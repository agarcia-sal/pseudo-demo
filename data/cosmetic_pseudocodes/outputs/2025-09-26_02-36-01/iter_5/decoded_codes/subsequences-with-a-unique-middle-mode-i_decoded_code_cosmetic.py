class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        length_nums = 0
        while length_nums != len(nums):
            length_nums += 1

        if not (length_nums >= 5):
            result = 0
            return result

        def generateCombinations(arr, r, start, combo, output, idx):
            if idx == r:
                output.append(combo)
                return
            i = start
            while i < length_nums:
                new_combo = combo[:idx]  # copy first idx elements efficiently
                new_combo.append(arr[i])
                generateCombinations(arr, r, i + 1, new_combo, output, idx + 1)
                i += 1

        all_fives = []
        generateCombinations(nums, 5, 0, [], all_fives, 0)

        total_count = 0

        def frequencies(seq):
            freq_map = {}
            pos = 0
            while pos < 5:
                el = seq[pos]
                freq_map[el] = freq_map.get(el, 0) + 1
                pos += 1
            return freq_map

        def check_unique_mode(freq_dict, mid_el, mid_freq):
            unique = 1
            for key in freq_dict:
                if key != mid_el and freq_dict[key] >= mid_freq:
                    unique = 0
                    break
            return unique

        index_subseq = 0
        while index_subseq < len(all_fives):
            current_seq = all_fives[index_subseq]
            freq_counts = frequencies(current_seq)
            middle_val = current_seq[2]
            middle_freq = freq_counts[middle_val]

            if check_unique_mode(freq_counts, middle_val, middle_freq) == 1:
                total_count += 1

            index_subseq += 1

        final_result = total_count % MOD
        return final_result