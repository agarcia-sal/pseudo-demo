class Solution:
    def maximumSumSubsequence(self, nums, queries):
        POW_TEN = 1_000_000_000
        MODULUS = POW_TEN + 1
        count = len(nums)
        carry_over_take = [0] * count
        carry_over_skip = [0] * count

        def InitializeDP():
            carry_over_take[0] = max(0, nums[0])
            carry_over_skip[0] = 0
            idx = 1
            while idx < count:
                carry_over_take[idx] = max(0, carry_over_skip[idx - 1] + nums[idx])
                carry_over_skip[idx] = max(carry_over_skip[idx - 1], carry_over_take[idx - 1])
                idx += 1

        def MaxFromTwo(a, b):
            return a if a > b else b

        def RefreshDPFrom(position):
            if position == 0:
                carry_over_take[0] = max(0, nums[0])
                carry_over_skip[0] = 0
            else:
                carry_over_take[position] = max(0, carry_over_skip[position - 1] + nums[position])
                carry_over_skip[position] = max(carry_over_skip[position - 1], carry_over_take[position - 1])

            def LoopFrom(idx):
                if idx >= count:
                    return
                carry_over_take[idx] = max(0, carry_over_skip[idx - 1] + nums[idx])
                carry_over_skip[idx] = max(carry_over_skip[idx - 1], carry_over_take[idx - 1])
                LoopFrom(idx + 1)

            LoopFrom(position + 1)

        InitializeDP()

        answer_accumulator = 0

        def ProcessQueriesRec(qs, index):
            nonlocal answer_accumulator
            if index >= len(qs):
                return
            current_pos, current_val = qs[index]
            nums[current_pos] = current_val
            RefreshDPFrom(current_pos)
            answer_accumulator = (answer_accumulator + MaxFromTwo(carry_over_take[count - 1], carry_over_skip[count - 1])) % MODULUS
            ProcessQueriesRec(qs, index + 1)

        ProcessQueriesRec(queries, 0)
        return answer_accumulator