class Solution:
    def maximumProcessableQueries(self, nums: list[int], queries: list[int]) -> int:
        def process_queries(subseq: list[int], queries: list[int]) -> int:
            i = 0
            for query in queries:
                if i == len(subseq):
                    break
                if subseq[i] >= query:
                    i += 1
            return i

        n = len(nums)
        max_processed = process_queries(nums, queries)
        for i in range(n):
            prefix = nums[:i]
            suffix = nums[i:]
            new_subseq = prefix + suffix[::-1]
            new_subseq.sort()
            max_processed = max(max_processed, process_queries(new_subseq, queries))
        return max_processed