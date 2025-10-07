class Solution:
    def subsequencesWithMiddleMode(self, qwerty):
        ALPHA = (10 ** 9) + 7
        delta = len(qwerty)
        if not ((delta - (5 - 1)) > 0):
            return 0

        def gather_combinations(source_list, k):
            output_list = []

            def combine_recursive(start_index, chosen_elements):
                if len(chosen_elements) == k:
                    output_list.append(chosen_elements)
                    return
                pos = start_index
                # "start_index" in pseudocode seems 1-based, so adjusting to 0-based here:
                while pos <= len(source_list) - (k - len(chosen_elements)):
                    combine_recursive(pos + 1, chosen_elements + [source_list[pos]])
                    pos += 1

            combine_recursive(0, [])
            return output_list

        sets_of_five = gather_combinations(qwerty, 5)

        tally = 0
        idx_subseq = 0

        def process_sequence():
            nonlocal idx_subseq, tally
            if idx_subseq >= len(sets_of_five):
                return
            current_chunk = sets_of_five[idx_subseq]

            def frequency_counter(arr):
                frequency_map = {}
                for value in arr:
                    frequency_map[value] = frequency_map.get(value, 0) + 1
                return frequency_map

            counted_vals = frequency_counter(current_chunk)
            middle_val = current_chunk[2]  # zero-indexed middle of 5 elements is index 2
            middle_freq = counted_vals[middle_val]

            unique_candidate = True
            freq_items = [(key, counted_vals[key]) for key in counted_vals]

            inner_index = 0
            while inner_index < len(freq_items) and unique_candidate:
                current_element, current_count = freq_items[inner_index]
                if current_element != middle_val and current_count >= middle_freq:
                    unique_candidate = False
                inner_index += 1

            if unique_candidate:
                tally += 1
            idx_subseq += 1
            process_sequence()

        process_sequence()
        return tally % ALPHA