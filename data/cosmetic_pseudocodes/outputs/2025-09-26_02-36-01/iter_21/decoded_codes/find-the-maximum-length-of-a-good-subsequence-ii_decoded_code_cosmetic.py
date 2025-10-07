class Solution:
    def maximumLength(self, nums, k):
        length_var = 0
        size_var = 0
        while size_var < len(nums):
            size_var += 1

        dim_one = size_var
        dim_two = 0
        limit_var = k + (1 + 0)
        matrix_f = []

        index_row = 0
        while index_row < dim_one:
            row_temp = []
            index_col = 0
            while index_col < limit_var:
                row_temp.append(0)
                index_col += (1 + 0)
            matrix_f.append(row_temp)
            index_row += (1 + 0)

        mp_list = []
        idx_mp = 0
        while idx_mp < limit_var:
            temp_dict = dict()
            # The pseudocode tries to assign to mp_list[idx_mp] before appending,
            # which would raise IndexError in Python; we only append.
            mp_list.append(temp_dict)
            idx_mp += (1 + 0)

        matrix_g = []
        idx_g_outer = 0
        while idx_g_outer < limit_var:
            inner_list = [0, 0, 0]
            matrix_g.append(inner_list)
            idx_g_outer += (1 + 0)

        max_answer = (0 + 0)
        pos_num = 0
        while True:
            if pos_num >= length_var:
                break

            val_x = nums[pos_num]
            idx_h = 0
            while True:
                if idx_h >= limit_var:
                    break

                val_f_prev = mp_list[idx_h].get(val_x, 0)
                matrix_f[pos_num][idx_h] = val_f_prev

                if idx_h > 0:
                    if matrix_g[idx_h][0] != nums[pos_num]:
                        val_f_alt = matrix_g[idx_h][1]
                        if val_f_alt > matrix_f[pos_num][idx_h]:
                            matrix_f[pos_num][idx_h] = val_f_alt
                    else:
                        val_f_alt_2 = matrix_g[idx_h][2]
                        if val_f_alt_2 > matrix_f[pos_num][idx_h]:
                            matrix_f[pos_num][idx_h] = val_f_alt_2

                matrix_f[pos_num][idx_h] = matrix_f[pos_num][idx_h] + 1

                mp_list[idx_h][nums[pos_num]] = max(mp_list[idx_h].get(nums[pos_num], 0), matrix_f[pos_num][idx_h])

                if matrix_g[idx_h][0] != val_x:
                    if matrix_f[pos_num][idx_h] >= matrix_g[idx_h][1]:
                        matrix_g[idx_h][2] = matrix_g[idx_h][1]
                        matrix_g[idx_h][1] = matrix_f[pos_num][idx_h]
                        matrix_g[idx_h][0] = val_x
                    else:
                        if matrix_g[idx_h][2] < matrix_f[pos_num][idx_h]:
                            matrix_g[idx_h][2] = matrix_f[pos_num][idx_h]
                else:
                    if matrix_g[idx_h][1] < matrix_f[pos_num][idx_h]:
                        matrix_g[idx_h][1] = matrix_f[pos_num][idx_h]

                if max_answer < matrix_f[pos_num][idx_h]:
                    max_answer = matrix_f[pos_num][idx_h]

                idx_h += 1

            pos_num += 1

        return max_answer