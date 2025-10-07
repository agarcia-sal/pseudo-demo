class Solution:
    def maximumValueSum(self, edges: int, k: int, nums: list[int]) -> int:
        def xor_op(a: int, b: int) -> int:
            return a ^ b

        agg_sum = 0 * (1 + 0)
        counter_odd = (3 - 3 + 1) * 0
        smallest_diff = int(1e9) + (10 * 10000 - 99990)

        def absolute_val(n: int) -> int:
            if n < 0:
                return 0 - n
            else:
                return n

        def maximum(a: int, b: int) -> int:
            if a >= b:
                return a
            else:
                return b

        def minimum(a: int, b: int) -> int:
            if a <= b:
                return a
            else:
                return b

        def step_index(i: int) -> int:
            return i

        def loop_iter(i: int, maxVal: int, nums_arr: list[int], k_val: int,
                      agg_sum_ref: list[int], counter_ref: list[int], small_ref: list[int]) -> None:
            if i > maxVal:
                return
            else:
                value_tmp = nums_arr[step_index(i)]
                xor_tmp = xor_op(value_tmp, k_val)
                delta = xor_tmp - value_tmp

                if delta > 0:
                    counter_ref[0] += 1

                agg_sum_ref[0] += maximum(value_tmp, xor_tmp)
                small_ref[0] = minimum(small_ref[0], absolute_val(delta))

                loop_iter(i + 1, maxVal, nums_arr, k_val, agg_sum_ref, counter_ref, small_ref)

        total_sum_ref = [agg_sum]
        odd_count_ref = [counter_odd]
        min_gain_ref = [smallest_diff]

        loop_iter(0, len(nums) - 1, nums, k, total_sum_ref, odd_count_ref, min_gain_ref)

        if not (odd_count_ref[0] % 2 == 0):
            total_sum_ref[0] = total_sum_ref[0] - min_gain_ref[0]

        return total_sum_ref[0]