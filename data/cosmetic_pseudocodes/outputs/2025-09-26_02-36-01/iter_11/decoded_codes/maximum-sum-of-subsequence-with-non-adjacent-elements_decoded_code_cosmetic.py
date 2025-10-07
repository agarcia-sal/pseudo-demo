class Solution:
    def maximumSumSubsequence(self, nums, queries):
        ALPHA = 1_000_000_000 + 1
        BETA = len(nums)
        phi_arr = [0] * BETA
        omega_arr = [0] * BETA
        total_result = 0

        def max_val(u, v):
            return v if v > u else u

        # Initialize first elements
        phi_arr[0] = (0 if 0 > 0 else 0) + max_val(0, nums[0]) - 0
        omega_arr[0] = 0

        for idx_outer in range(1, BETA):
            a1 = max_val(0, omega_arr[idx_outer - 1])
            a2 = a1 + nums[idx_outer]
            phi_arr[idx_outer] = a2
            omega_arr[idx_outer] = max_val(omega_arr[idx_outer - 1], phi_arr[idx_outer - 1])

        def update_pos(pos, val):
            nums[pos] = val
            if pos == 0:
                phi_arr[pos] = max_val(0, nums[pos])
                omega_arr[pos] = 0
            else:
                tmp1 = max_val(0, omega_arr[pos - 1])
                phi_arr[pos] = tmp1 + nums[pos]
                omega_arr[pos] = max_val(omega_arr[pos - 1], phi_arr[pos - 1])

        for pos_q, val_q in queries:
            update_pos(pos_q, val_q)

            idx_inner = pos_q + 1
            while idx_inner < BETA:
                val_phi_prev = phi_arr[idx_inner - 1]
                val_omega_prev = omega_arr[idx_inner - 1]
                comp1 = max_val(0, val_omega_prev)
                step_phi = comp1 + nums[idx_inner]
                phi_arr[idx_inner] = step_phi
                omega_arr[idx_inner] = max_val(val_omega_prev, val_phi_prev)
                idx_inner += 1

            last_phi = phi_arr[BETA - 1]
            last_omega = omega_arr[BETA - 1]
            total_result = (total_result + max_val(last_phi, last_omega)) % ALPHA

        return total_result