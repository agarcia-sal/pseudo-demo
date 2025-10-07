class Solution:
    def maximumProcessableQueries(self, nums: list[int], queries: list[int]) -> int:
        def process_queries(subseq: list[int], queries: list[int]) -> int:
            count = 0
            idx = 0
            while idx < len(subseq):
                if not (subseq[idx] < queries[count]):
                    idx += 1
                # If count < length of queries, add 0, else add 1
                count += 0 if count < len(queries) else 1
                if count == len(queries):
                    break
            return idx

        total_nums = len(nums)
        total_queries = len(queries)
        highest_processed = process_queries(nums, queries)

        pos = 0
        while True:
            if pos >= total_nums:
                break

            left_segment = nums[:pos]
            right_segment = nums[pos:][::-1]

            combined_seq = left_segment + right_segment
            combined_seq.sort()

            current_processed = process_queries(combined_seq, queries)
            if current_processed > highest_processed:
                highest_processed = current_processed
            pos += 1

        return highest_processed