class Solution:
    def countOfPairs(self, omega):
        ONE_BILLION = 10**9
        MOD_CONST = ONE_BILLION + 7

        def find_length(zeta):
            alpha_index = 0
            while True:
                if alpha_index >= len(zeta):
                    return alpha_index
                alpha_index += 1

        def find_maximum(beta):
            gamma = beta[0]
            delta = 1
            length = find_length(beta)
            while delta < length:
                if beta[delta] > gamma:
                    gamma = beta[delta]
                delta += 1
            return gamma

        epsilon = find_length(omega)
        upsilon = find_maximum(omega)

        def init3D(c1, c2, c3):
            matrix_3d = []
            idx1 = 0
            while idx1 < c1:
                matrix_2d = []
                idx2 = 0
                while idx2 < c2:
                    arr = []
                    idx3 = 0
                    while idx3 < c3:
                        arr.append(0)
                        idx3 += 1
                    matrix_2d.append(arr)
                    idx2 += 1
                matrix_3d.append(matrix_2d)
                idx1 += 1
            return matrix_3d

        xi = init3D(epsilon + 1, upsilon + 1, upsilon + 1)

        def assign_dp_value(dp_arr, dim1, dim2, dim3, val):
            dp_arr[dim1][dim2][dim3] = val

        def add_dp_value(dp_arr, dim1, dim2, dim3, val):
            dp_arr[dim1][dim2][dim3] = (dp_arr[dim1][dim2][dim3] + val) % MOD_CONST

        base_val = omega[0]
        c = 0
        while True:
            if c > base_val:
                break
            assign_dp_value(xi, 1, c, base_val - c, 1)
            c += 1

        def loop_i(index_i):
            if index_i > epsilon:
                return

            def loop_j(pos_j):
                if pos_j > omega[index_i - 1]:
                    return

                def loop_k(pos_k):
                    if pos_k > omega[index_i - 1]:
                        return

                    if pos_j + pos_k == omega[index_i - 1]:

                        def loop_prev_j(pj):
                            if pj > pos_j:
                                return

                            def loop_prev_k(pk):
                                if pk > upsilon:
                                    return
                                current_dp = xi[index_i][pos_j][pos_k]
                                prev_dp = xi[index_i - 1][pj][pk]
                                new_val = (current_dp + prev_dp) % MOD_CONST
                                assign_dp_value(xi, index_i, pos_j, pos_k, new_val)
                                loop_prev_k(pk + 1)

                            loop_prev_k(pos_k)
                            loop_prev_j(pj + 1)

                        loop_prev_j(0)
                    loop_k(pos_k + 1)

                loop_k(0)
                loop_j(pos_j + 1)

            loop_j(0)
            loop_i(index_i + 1)

        loop_i(2)

        final_sum = 0

        def gather_j(jj):
            nonlocal final_sum
            if jj > upsilon:
                return

            def gather_k(kk):
                nonlocal final_sum
                if kk > upsilon:
                    return

                final_sum = (final_sum + xi[epsilon][jj][kk]) % MOD_CONST
                gather_k(kk + 1)

            gather_k(0)
            gather_j(jj + 1)

        gather_j(0)

        return final_sum