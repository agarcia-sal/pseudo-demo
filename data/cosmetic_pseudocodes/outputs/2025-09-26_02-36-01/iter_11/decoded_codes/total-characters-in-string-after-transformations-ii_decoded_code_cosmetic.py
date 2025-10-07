class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        R9 = 1_000_000_001

        # Initialize 26x26 zero matrix
        alpha_matrix = [[0] * 26 for _ in range(26)]

        # Build alpha_matrix based on nums
        for index1 in range(26):
            for index2 in range(nums[index1]):
                tgt_pos = (index1 + index2 + 1) % 26
                alpha_matrix[index1][tgt_pos] += 1

        def dotMultiply(M1: list[list[int]], M2: list[list[int]]) -> list[list[int]]:
            res_matrix = [[0] * 26 for _ in range(26)]
            for a in range(26):
                row_M1 = M1[a]
                for b in range(26):
                    acc = 0
                    for c in range(26):
                        acc += row_M1[c] * M2[c][b]
                    res_matrix[a][b] = acc % R9
            return res_matrix

        def powerMatrix(baseM: list[list[int]], exponent: int) -> list[list[int]]:
            # Identity matrix
            result_matrix = [[0] * 26 for _ in range(26)]
            for i in range(26):
                result_matrix[i][i] = 1

            base_clone = baseM
            e = exponent
            while e > 0:
                if e & 1:
                    result_matrix = dotMultiply(result_matrix, base_clone)
                base_clone = dotMultiply(base_clone, base_clone)
                e >>= 1
            return result_matrix

        exp_matrix = powerMatrix(alpha_matrix, t)

        char_counts = [0] * 26
        for ch in s:
            char_counts[ord(ch) - ord('a')] += 1

        agg_counts = [0] * 26
        for idx_outer in range(26):
            count_outer = char_counts[idx_outer]
            if count_outer == 0:
                continue
            row_exp = exp_matrix[idx_outer]
            for idx_inner in range(26):
                agg_counts[idx_inner] = (agg_counts[idx_inner] + count_outer * row_exp[idx_inner]) % R9

        sum_result = 0
        for val in agg_counts:
            sum_result = (sum_result + val) % R9

        return sum_result