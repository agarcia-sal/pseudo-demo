class Solution:
    def countOfPairs(self, nums):
        const_mod = 10**9 + 7
        size_val = len(nums)
        peak = nums[0]
        for idx in range(1, size_val):
            if nums[idx] > peak:
                peak = nums[idx]

        # Initialize 3D list with zeros
        # dimensions: (size_val+1) x (peak+1) x (peak+1)
        states = [[[0]*(peak+1) for _ in range(peak+1)] for __ in range(size_val+1)]

        pos0 = nums[0]
        counter = 0
        while counter <= pos0:
            states[1][counter][pos0 - counter] = 1
            counter += 1

        outer_idx = 2
        while outer_idx <= size_val:
            curr_val = nums[outer_idx - 1]
            mid_j = 0
            while mid_j <= curr_val:
                mid_k = 0
                while mid_k <= curr_val:
                    if (mid_j + mid_k) == curr_val:
                        left_j = 0
                        while left_j <= mid_j:
                            left_k = mid_k
                            while left_k <= peak:
                                current_state = states[outer_idx][mid_j][mid_k]
                                previous_state = states[outer_idx - 1][left_j][left_k]
                                updated_value = current_state + previous_state
                                if updated_value >= const_mod:
                                    updated_value -= const_mod
                                states[outer_idx][mid_j][mid_k] = updated_value
                                left_k += 1
                            left_j += 1
                    mid_k += 1
                mid_j += 1
            outer_idx += 1

        acc_result = 0
        ind_j = 0
        while ind_j <= peak:
            ind_k = 0
            while ind_k <= peak:
                acc_result += states[size_val][ind_j][ind_k]
                if acc_result >= const_mod:
                    acc_result -= const_mod
                ind_k += 1
            ind_j += 1

        return acc_result