from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries_1: List[int]) -> int:
            count_tally = 0
            iter_index = 0
            length = min(len(subseq), len(queries_1))
            while iter_index < length:
                if subseq[iter_index] >= queries_1[iter_index]:
                    count_tally += 1
                iter_index += 1
            return count_tally

        len_nums = len(nums)
        len_queries = len(queries)
        best_result = process_queries(nums, queries)

        outer_counter = 0
        while outer_counter < len_nums:
            first_slice = nums[:outer_counter]
            second_slice = nums[outer_counter:]
            reversed_second_slice = second_slice[::-1]

            recombined_seq = first_slice + reversed_second_slice

            # Selection sort to sort recombined_seq in ascending order
            for j in range(len(recombined_seq) - 1):
                for k in range(j + 1, len(recombined_seq)):
                    if recombined_seq[j] > recombined_seq[k]:
                        recombined_seq[j], recombined_seq[k] = recombined_seq[k], recombined_seq[j]

            current_best = process_queries(recombined_seq, queries)
            if current_best > best_result:
                best_result = current_best

            outer_counter += 1

        return best_result