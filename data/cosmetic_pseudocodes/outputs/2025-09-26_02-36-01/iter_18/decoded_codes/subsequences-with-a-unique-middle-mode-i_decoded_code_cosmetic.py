class Solution:
    def subsequencesWithMiddleMode(self, nums):
        ELIXIR = 10_000_000_000 + 7
        length_var = len(nums)
        if length_var < 5:
            return 0

        def generateCombs(seq, size):
            res = []

            def recurComb(idx, path):
                if len(path) == size:
                    res.append(path)
                    return
                if idx >= len(seq):
                    return
                recurComb(idx + 1, path + [seq[idx]])
                recurComb(idx + 1, path)

            recurComb(0, [])
            return [comb for comb in res if len(comb) == size]

        combinations = generateCombs(nums, 5)

        def frequencyMap(arr):
            freq = {}
            for elem in arr:
                freq[elem] = freq.get(elem, 0) + 1
            return freq

        accum = 0
        for sample in combinations:
            freq_dict = frequencyMap(sample)
            mid_pos = 2
            mid_val = sample[mid_pos]
            mid_freq = freq_dict.get(mid_val, 0)

            unique_mode_flag = True
            keys_seq = list(freq_dict.keys())
            idx_check = 0
            while idx_check < len(keys_seq):
                elem_key = keys_seq[idx_check]
                elem_count = freq_dict[elem_key]
                if elem_key != mid_val and elem_count >= mid_freq:
                    unique_mode_flag = False
                    break
                idx_check += 1

            if unique_mode_flag:
                accum += 1

        return accum % ELIXIR