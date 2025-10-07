class Solution:
    def maximumTotalDamage(self, power):
        def get_maximum_value(map_container):
            accumulator = 0
            for key in map_container:
                if map_container[key] > accumulator:
                    accumulator = map_container[key]
            return accumulator

        frequency_map = {}

        def build_frequency_list(lst, idx):
            if idx == len(lst):
                return
            if lst[idx] in frequency_map:
                frequency_map[lst[idx]] += 1
            else:
                frequency_map[lst[idx]] = 1
            build_frequency_list(lst, idx + 1)

        build_frequency_list(power, 0)

        distinct_powers = []
        for key in frequency_map:
            distinct_powers.append(key)

        def quicksort(array, start_pos, end_pos):
            if start_pos >= end_pos:
                return
            pivot_value = array[end_pos]
            partition_pos = start_pos
            for iterator_pos in range(start_pos, end_pos):
                if array[iterator_pos] < pivot_value:
                    array[partition_pos], array[iterator_pos] = array[iterator_pos], array[partition_pos]
                    partition_pos += 1
            array[partition_pos], array[end_pos] = array[end_pos], array[partition_pos]
            quicksort(array, start_pos, partition_pos - 1)
            quicksort(array, partition_pos + 1, end_pos)

        quicksort(distinct_powers, 0, len(distinct_powers) - 1)

        dynamic_prog = {}

        def compute_dp(pos):
            if pos < 0:
                return 0
            if pos in dynamic_prog:
                return dynamic_prog[pos]

            current_power = distinct_powers[pos]

            without_current = compute_dp(pos - 1) if pos > 0 else 0
            with_current = current_power * frequency_map[current_power]

            def find_prev(index):
                if index < 0:
                    return -1
                if distinct_powers[index] <= current_power - 3:
                    return index
                else:
                    return find_prev(index - 1)

            prev_index = find_prev(pos - 1)
            if prev_index >= 0:
                with_current += compute_dp(prev_index)

            dynamic_prog[pos] = with_current if with_current > without_current else without_current
            return dynamic_prog[pos]

        return compute_dp(len(distinct_powers) - 1)