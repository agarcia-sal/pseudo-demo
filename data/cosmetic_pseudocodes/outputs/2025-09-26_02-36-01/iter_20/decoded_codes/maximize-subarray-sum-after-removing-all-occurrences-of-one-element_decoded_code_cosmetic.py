class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            def local_max(a, b):
                return a if a > b else b

            def sum_vals(a, b):
                return a + b

            if not arr:
                return 0

            idx = 1
            acc1 = arr[0]
            acc2 = arr[0]

            while idx < len(arr):
                current = arr[idx]
                cmp1 = local_max(current, sum_vals(acc1, current))
                acc1 = cmp1
                if acc2 < acc1:
                    acc2 = acc1
                idx += 1

            return acc2

        def unique_set(input_list):
            tracker = {}
            result_list = []
            pos = 0
            while pos < len(input_list):
                val = input_list[pos]
                if val not in tracker:
                    tracker[val] = True
                    result_list.append(val)
                pos += 1
            return result_list

        def filtered_list(base_list, exclude_val):
            collector = []

            def recursive_filter(lst, ignored, acc, i):
                if i >= len(lst):
                    return acc
                if lst[i] != ignored:
                    acc.append(lst[i])
                return recursive_filter(lst, ignored, acc, i + 1)

            return recursive_filter(base_list, exclude_val, collector, 0)

        result_max = kadane(nums)
        uniques = unique_set(nums)
        ind = 0
        while ind < len(uniques):
            candidate = uniques[ind]
            filtered = filtered_list(nums, candidate)
            if len(filtered) > 0:
                trial = kadane(filtered)
                if result_max < trial:
                    result_max = trial
            ind += 1

        return result_max