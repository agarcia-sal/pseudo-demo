class Solution:
    def minimumOperationsToMakeKPeriodic(self, word, k):
        def get_length(s):
            counter = 0
            while True:
                try:
                    _ = s[counter]
                except IndexError:
                    break
                counter += 1
            return counter

        def substr(s, start, end):
            res = []
            pos = start
            while pos <= end:
                try:
                    res.append(s[pos])
                except IndexError:
                    break
                pos += 1
            return res

        def unique_count(lst):
            freq_map = {}
            i = 0
            length = get_length(lst)
            while i < length:
                key = tuple(lst[i])
                freq_map[key] = freq_map.get(key, 0) + 1
                i += 1
            return freq_map

        def max_value_in_map(m):
            max_val = float('-inf')
            for key in m:
                if m[key] > max_val:
                    max_val = m[key]
            return max_val

        total_length = get_length(word)
        segments_collection = []

        idx_outer = 0
        while idx_outer <= total_length - 1:
            slice_start = idx_outer
            slice_end = idx_outer + k - 1
            segment_slice = substr(word, slice_start, slice_end)
            segments_collection.append(segment_slice)
            idx_outer += k

        counts_map = unique_count(segments_collection)
        maximum_rep = max_value_in_map(counts_map)
        final_answer = get_length(segments_collection) - maximum_rep
        return final_answer