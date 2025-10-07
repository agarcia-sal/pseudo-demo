from typing import List

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        alpha = 1 << 7  # 128
        beta = len(nums)

        # Initialize gamma: 3D list of bools, dimensions (beta+1) x (k+2) x alpha
        gamma = [[[False] * alpha for _ in range(k + 2)] for _ in range(beta + 1)]
        gamma[0][0][0] = True

        for idx_i in range(beta):
            for idx_j in range(k + 1):
                gamma_i_j = gamma[idx_i][idx_j]
                gamma_next_j = gamma[idx_i + 1][idx_j]
                gamma_next_jp1 = gamma[idx_i + 1][idx_j + 1]
                num = nums[idx_i]
                for idx_x in range(alpha):
                    if gamma_i_j[idx_x]:
                        gamma_next_j[idx_x] = True
                        gamma_next_jp1[idx_x | num] = True

        # Initialize delta
        delta = [[[False] * alpha for _ in range(k + 2)] for _ in range(beta + 1)]
        delta[beta][0][0] = True

        loop_i = beta
        while loop_i > 0:
            for loop_j in range(k + 1):
                delta_i_j = delta[loop_i][loop_j]
                delta_prev_j = delta[loop_i - 1][loop_j]
                delta_prev_jp1 = delta[loop_i - 1][loop_j + 1]
                num = nums[loop_i - 1]
                for loop_y in range(alpha):
                    if delta_i_j[loop_y]:
                        delta_prev_j[loop_y] = True
                        delta_prev_jp1[loop_y | num] = True
            loop_i -= 1

        result = 0
        for u in range(k, beta - k + 1):
            gamma_u_k = gamma[u][k]
            delta_u_k = delta[u][k]
            for v in range(alpha):
                if gamma_u_k[v]:
                    for w in range(alpha):
                        if delta_u_k[w]:
                            tempVal = v ^ w
                            if tempVal > result:
                                result = tempVal

        return result