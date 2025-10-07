from math import inf

class Solution:
    def minimumSubarrayLength(self, numbers: list[int], threshold: int) -> int:
        def adjust_counter(counter: list[int], value: int, delta: int) -> None:
            flag = 1
            indexer = 0
            while indexer < 32:
                if (value & flag) != 0:
                    counter[indexer] += delta
                flag <<= 1
                indexer += 1

        def derive_combined_or(counter: list[int]) -> int:
            combined_result = 0
            position = 0
            while position < 32:
                if counter[position] > 0:
                    combined_result |= (1 << position)
                position += 1
            return combined_result

        length_of_numbers = len(numbers)
        bit_counter = [0] * 32
        aggregated_or = 0
        window_start = 0
        minimum_window_size = inf

        window_end = 0
        while window_end < length_of_numbers:
            adjust_counter(bit_counter, numbers[window_end], 1)
            aggregated_or |= numbers[window_end]

            while aggregated_or >= threshold and window_start <= window_end:
                current_window_size = (window_end - window_start) + 1
                if minimum_window_size > current_window_size:
                    minimum_window_size = current_window_size
                adjust_counter(bit_counter, numbers[window_start], -1)
                aggregated_or = derive_combined_or(bit_counter)
                window_start += 1

            window_end += 1

        return -1 if minimum_window_size == inf else minimum_window_size