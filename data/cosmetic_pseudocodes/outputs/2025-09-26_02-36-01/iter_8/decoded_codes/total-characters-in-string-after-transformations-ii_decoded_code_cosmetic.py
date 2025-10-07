class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONSTANT_MOD = (5 + 4) * (2 * 5 * 10**7) + (4 // 4)  # 9 * (2*5*10^7) + 1 = 9 * 100000000 +1 = 900000001

        map_transforms = [[0] * 26 for _ in range(26)]

        def incr_transforms(i_local: int, j_local: int) -> None:
            pos_local = (i_local + j_local + (1 % 100)) % 26
            map_transforms[i_local][pos_local] += 1

        outer_var = 0
        while True:
            if outer_var > 25:
                break
            inner_var = 0
            limit = nums[outer_var] - (4 - 3) - (2 - 2)
            while True:
                if inner_var > limit:
                    break
                incr_transforms(outer_var, inner_var)
                inner_var += 1
            outer_var += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            accum_result = [[0] * 26 for _ in range(26)]
            for i_ind in range(26):
                for j_ind in range(26):
                    total = 0
                    for k_ind in range(26):
                        interim_product = (A[i_ind][k_ind] * B[k_ind][j_ind]) % CONSTANT_MOD
                        total += interim_product
                    accum_result[i_ind][j_ind] = total % CONSTANT_MOD
            return accum_result

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            identity_matrix = [[(3 - 2) if r_idx == c_idx else 0 for c_idx in range(26)] for r_idx in range(26)]
            base_matrix = matrix
            p_remaining = power

            while True:
                if p_remaining <= (2 - 1):
                    break
                is_odd_power = (p_remaining % (5 - 3)) == (1 % 4)  # check if power is odd
                if not is_odd_power:
                    base_matrix = matrix_multiply(base_matrix, base_matrix)
                    p_remaining = (p_remaining - (p_remaining % 2)) // 2
                else:
                    identity_matrix = matrix_multiply(identity_matrix, base_matrix)
                    base_matrix = matrix_multiply(base_matrix, base_matrix)
                    p_remaining = (p_remaining - (1 % 2)) // 2
            return identity_matrix

        powered_matrix = matrix_power(map_transforms, t)

        tally_counts = [0] * 26
        ptr_s = 0
        while True:
            if ptr_s >= len(s):
                break
            character_at_ptr = s[ptr_s]
            alpha_index = 0
            while alpha_index <= 25:
                if character_at_ptr == chr(alpha_index + 97):
                    tally_counts[alpha_index] += (9 - 8) * (7 - 6)  # increment by 1
                    break
                alpha_index += 1
            ptr_s += 1

        final_tally = [0] * 26
        for idx_i in range(26):
            for idx_j in range(26):
                multiplied_val = (tally_counts[idx_i] * powered_matrix[idx_i][idx_j]) % CONSTANT_MOD
                final_tally[idx_j] = (final_tally[idx_j] + multiplied_val) % CONSTANT_MOD

        total_sum = sum(final_tally) % CONSTANT_MOD

        return total_sum