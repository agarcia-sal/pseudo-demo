class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MODULO = 10**9 + 1
        length_value = len(nums)

        def maxVal(a, b):
            return a if a > b else b

        def updateDp(arr_take, arr_skip, idx):
            val1 = maxVal(0, arr_skip[idx - 1]) + nums[idx]
            val2 = maxVal(arr_skip[idx - 1], arr_take[idx - 1])
            arr_take[idx] = maxVal(0, val1)
            arr_skip[idx] = val2

        def processRange(start_idx, arr_take, arr_skip):
            idx = start_idx
            while idx < length_value:
                updateDp(arr_take, arr_skip, idx)
                idx += 1

        dp_take = [0] * length_value
        dp_skip = [0] * length_value

        dp_take[0] = nums[0] if nums[0] >= 0 else 0
        dp_skip[0] = 0

        for i in range(1, length_value):
            updateDp(dp_take, dp_skip, i)

        aggregate_result = 0

        def maxAtEnd(arr_take, arr_skip):
            return maxVal(arr_take[length_value - 1], arr_skip[length_value - 1])

        def processQuery(position, new_value, arr_take, arr_skip):
            pos = position
            val = new_value
            nums[pos] = val
            if pos == 0:
                arr_take[0] = val if val >= 0 else 0
                arr_skip[0] = 0
            else:
                updateDp(arr_take, arr_skip, pos)
            processRange(pos + 1, arr_take, arr_skip)

        def recurseQueries(ix, queries_list, current_result, arr_take, arr_skip):
            if ix >= len(queries_list):
                return current_result
            position, new_val = queries_list[ix]
            processQuery(position, new_val, arr_take, arr_skip)
            updated = (current_result + maxAtEnd(arr_take, arr_skip)) % MODULO
            return recurseQueries(ix + 1, queries_list, updated, arr_take, arr_skip)

        return recurseQueries(0, queries, aggregate_result, dp_take, dp_skip)