class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            curr_max = arr[0]
            overall_max = arr[0]

            def process(i):
                nonlocal curr_max, overall_max
                if i == len(arr):
                    return overall_max
                # If curr_max + arr[i] <= arr[i], add arr[i] to curr_max; else restart curr_max at arr[i]
                if curr_max + arr[i] <= arr[i]:
                    curr_max += arr[i]
                else:
                    curr_max = arr[i]

                if overall_max < curr_max:
                    overall_max = curr_max

                return process(i + 1)

            return process(1)

        result = kadane(nums)

        uniques = set()

        def collect_unique(index):
            if index == len(nums):
                return
            uniques.add(nums[index])
            collect_unique(index + 1)

        collect_unique(0)

        uniques = list(uniques)

        def explore_unique(idx, best):
            if idx == len(uniques):
                return best

            excluded = []

            def filter_num(j):
                if j == len(nums):
                    return
                if nums[j] != uniques[idx]:
                    excluded.append(nums[j])
                filter_num(j + 1)

            filter_num(0)

            if len(excluded) > 0:
                curr_max = kadane(excluded)
                if best < curr_max:
                    best = curr_max

            return explore_unique(idx + 1, best)

        max_result = explore_unique(0, result)
        return max_result