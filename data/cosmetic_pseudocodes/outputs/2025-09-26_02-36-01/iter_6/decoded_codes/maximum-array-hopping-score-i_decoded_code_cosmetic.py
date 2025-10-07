class Solution:
    def maxScore(self, nums):
        len_nums = len(nums)
        result_arr = [0] * len_nums
        result_arr[1] = 0

        def inner_loop(curr_outer, curr_inner):
            if not (curr_inner < curr_outer):
                return
            temp_val_a = result_arr[curr_outer]
            temp_val_b = result_arr[curr_inner] + (curr_outer - curr_inner) * nums[curr_outer]
            if temp_val_a < temp_val_b:
                result_arr[curr_outer] = temp_val_b
            inner_loop(curr_outer, curr_inner + 1)

        def outer_loop(curr_outer):
            if not (curr_outer <= len_nums - 1):
                return
            inner_loop(curr_outer, 1)
            outer_loop(curr_outer + 1)

        outer_loop(2)
        return result_arr[len_nums - 1]