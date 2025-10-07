from bisect import bisect_left

class Solution:
    def maximumProcessableQueries(self, nums: list[int], queries: list[int]) -> int:
        def process_queries(subseq: list[int], queries: list[int]) -> int:
            idx = 0
            iter_q = 0
            len_subseq = len(subseq)
            len_queries = len(queries)
            while True:
                if idx == len_subseq:
                    break
                if subseq[idx] >= queries[iter_q]:
                    idx += 1
                iter_q += 1
                if iter_q == len_queries:
                    break
            return idx

        length_nums = len(nums)
        length_queries = len(queries)
        best_result = process_queries(nums, queries)

        counter = 0
        while counter < length_nums:
            front_part = nums[:counter]
            back_part = nums[counter:]
            reversed_back = back_part[::-1]
            combined_list = front_part + reversed_back
            combined_list.sort()

            candidate_result = process_queries(combined_list, queries)
            if candidate_result > best_result:
                best_result = candidate_result
            counter += 1

        return best_result