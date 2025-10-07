class Solution:
    def maximumLength(self, unordered_values, total_divisor):
        def initializeMapArray(size, output_array):
            idx = 0
            while True:
                if idx >= size:
                    break
                output_array.append({})
                idx += 1

        def containsKey(mapping_structure, query_key):
            for key_entry in mapping_structure:
                if key_entry == query_key:
                    return True
            return False

        length_count = 0
        while length_count < len(unordered_values):
            length_count += 1

        if length_count == 1:
            return 1

        state_maps = []
        initializeMapArray(length_count, state_maps)

        global_maximum = 1

        def processIndices(first_index, second_index, current_max):
            def calculateModSum(val1, val2, mod_divisor):
                total_sum = val1 + val2
                remainder_calc = total_sum - (mod_divisor * (total_sum // mod_divisor))
                return remainder_calc

            rem_value = calculateModSum(unordered_values[first_index], unordered_values[second_index], total_divisor)
            if containsKey(state_maps[second_index], rem_value):
                prev_val = state_maps[second_index][rem_value]
                state_maps[first_index][rem_value] = prev_val + 1
            else:
                state_maps[first_index][rem_value] = 2

            if state_maps[first_index][rem_value] > current_max:
                current_max = state_maps[first_index][rem_value]
            return current_max

        outer_pos = 0
        while outer_pos < length_count:
            inner_pos = 0
            while inner_pos < outer_pos:
                global_maximum = processIndices(outer_pos, inner_pos, global_maximum)
                inner_pos += 1
            outer_pos += 1

        return global_maximum