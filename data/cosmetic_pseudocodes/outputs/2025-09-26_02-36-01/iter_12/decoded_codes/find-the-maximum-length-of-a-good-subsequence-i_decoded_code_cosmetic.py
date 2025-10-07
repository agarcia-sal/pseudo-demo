class Solution:
    def maximumLength(self, nums, k):
        length_val = 0  # Unused variable, kept for faithful translation
        total_elements = len(nums)
        matrix_f = []

        # Initialize matrix_f with 1s, size total_elements x (k+1)
        for _ in range(total_elements):
            inner_list = [1] * (k + 1)
            matrix_f.append(inner_list)

        max_length = 0
        for idx_i in range(total_elements):
            current_element = nums[idx_i]
            for idx_h in range(k + 1):
                for idx_j in range(idx_i):
                    compare_element = nums[idx_j]
                    if current_element == compare_element:
                        if matrix_f[idx_i][idx_h] < matrix_f[idx_j][idx_h] + 1:
                            matrix_f[idx_i][idx_h] = matrix_f[idx_j][idx_h] + 1
                    else:
                        if idx_h > 0:
                            if matrix_f[idx_i][idx_h] < matrix_f[idx_j][idx_h - 1] + 1:
                                matrix_f[idx_i][idx_h] = matrix_f[idx_j][idx_h - 1] + 1
            if max_length < matrix_f[idx_i][k]:
                max_length = matrix_f[idx_i][k]

        return max_length