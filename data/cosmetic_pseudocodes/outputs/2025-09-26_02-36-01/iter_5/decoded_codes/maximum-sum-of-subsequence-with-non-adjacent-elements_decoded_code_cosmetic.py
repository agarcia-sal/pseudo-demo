class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MODULO = 10**9 + 1
        length_nums = len(nums)

        dp_take = [0] * length_nums
        dp_skip = [0] * length_nums

        def fillArrays(pos):
            if pos < 1:
                dp_take[0] = nums[0] if nums[0] > 0 else 0
                dp_skip[0] = 0
            else:
                prev_skip = dp_skip[pos - 1] if dp_skip[pos - 1] > 0 else 0
                dp_take[pos] = prev_skip + nums[pos]
                dp_skip[pos] = max(dp_skip[pos - 1], dp_take[pos - 1])

        def propagateUpdate(index):
            if index >= length_nums:
                return
            fillArrays(index)
            propagateUpdate(index + 1)

        fillArrays(0)
        for i in range(1, length_nums):
            fillArrays(i)

        accumulator_result = 0

        def processQuery(pos, new_val):
            nonlocal accumulator_result
            nums[pos] = new_val
            fillArrays(pos)
            propagateUpdate(pos + 1)
            max_end = dp_take[length_nums - 1] if dp_take[length_nums - 1] > dp_skip[length_nums - 1] else dp_skip[length_nums - 1]
            accumulator_result = (accumulator_result + max_end) % MODULO

        ptr = 0
        while ptr < len(queries):
            curr_pos, value_new = queries[ptr]
            processQuery(curr_pos, value_new)
            ptr += 1

        return accumulator_result