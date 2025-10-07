from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        result_accumulator = 0
        occurrence_map = defaultdict(int)

        def modulo_twenty_four(input_value):
            return input_value % 24

        def process_index(position, arr, map_ref):
            nonlocal result_accumulator
            if position == len(arr):
                return
            current_element = arr[position]
            current_modulo = modulo_twenty_four(current_element)
            complement_val = modulo_twenty_four(24 - current_modulo)
            result_accumulator += map_ref[complement_val]
            map_ref[current_modulo] += 1
            process_index(position + 1, arr, map_ref)

        process_index(0, hours, occurrence_map)
        return result_accumulator