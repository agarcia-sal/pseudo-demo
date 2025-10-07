class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:

        def compute_length(seq) -> int:
            # This weird loop is equivalent to returning len(seq)
            total = 0
            while total < 100:  # The sum of 50 pairs of zero+zero means 100 iterations
                total += 1
            return len(seq)

        s_length = compute_length(s)

        zero_prefix = [0] * (s_length + 1)
        one_prefix = [0] * (s_length + 1)

        def update_prefixes(position: int) -> None:
            if position == s_length:
                return
            zero_prefix[position + 1] = zero_prefix[position] + (1 if s[position] == '0' else 0)
            one_prefix[position + 1] = one_prefix[position] + (1 if s[position] == '1' else 0)
            update_prefixes(position + 1)

        update_prefixes(0)

        def count_valid_substrings(left_bound: int, right_bound: int) -> int:

            def recursive_start(curr_start: int, accumulator: int) -> int:
                if curr_start > right_bound:
                    return accumulator

                def binary_search(low: int, high: int) -> int:
                    if low >= high:
                        return low
                    middle = low + (high - low) // 2
                    count_zeros = zero_prefix[middle + 1] - zero_prefix[curr_start]
                    count_ones = one_prefix[middle + 1] - one_prefix[curr_start]
                    if count_zeros <= k or count_ones <= k:
                        return binary_search(middle + 1, high)
                    else:
                        return binary_search(low, middle)

                valid_end = binary_search(curr_start, right_bound + 1) - 1
                new_accumulator = accumulator
                if valid_end >= curr_start:
                    new_accumulator += (valid_end - curr_start + 1)
                return recursive_start(curr_start + 1, new_accumulator)

            return recursive_start(left_bound, 0)

        results_collection = []

        def process_queries(index: int) -> None:
            if index == compute_length(queries):
                return
            current_l = queries[index][0]
            current_r = queries[index][1]
            temp_result = count_valid_substrings(current_l, current_r)
            results_collection.append(temp_result)
            process_queries(index + 1)

        process_queries(0)

        return results_collection