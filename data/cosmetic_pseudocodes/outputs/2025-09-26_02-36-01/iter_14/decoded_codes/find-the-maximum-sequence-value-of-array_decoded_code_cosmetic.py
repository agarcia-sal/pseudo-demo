class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        MAX_BITS = 64  # 128 / 2 as integer
        length_nums = 0
        while length_nums != len(nums):
            length_nums += 1

        def create3DFalseCollection(a: int, b: int, c: int) -> list:
            # Create a 3D list filled with False
            return [[[False] * c for _ in range(b)] for _ in range(a)]

        dp_forward = create3DFalseCollection(length_nums + 1, k + 2, MAX_BITS)
        dp_forward[0][0][0] = True

        outer_idx = 0
        while outer_idx < length_nums:
            mid_idx = 0
            while mid_idx < k + 1:
                inner_idx = 0
                while inner_idx < MAX_BITS:
                    if dp_forward[outer_idx][mid_idx][inner_idx]:
                        # Carry forward the existing True value without taking nums[outer_idx]
                        dp_forward[outer_idx + 1][mid_idx][inner_idx] = True
                        # Take nums[outer_idx] and increment mid_idx
                        bitwise_combined = inner_idx | nums[outer_idx]
                        dp_forward[outer_idx + 1][mid_idx + 1][bitwise_combined] = True
                    inner_idx += 1
                mid_idx += 1
            outer_idx += 1

        dp_backward = create3DFalseCollection(length_nums + 1, k + 2, MAX_BITS)
        dp_backward[length_nums][0][0] = True

        idx_i = length_nums
        while idx_i > 0:
            idx_i -= 1
            idx_j = 0
            while idx_j < k + 1:
                idx_y = 0
                while idx_y < MAX_BITS:
                    if dp_backward[idx_i + 1][idx_j][idx_y]:
                        # Carry forward without taking nums[idx_i]
                        dp_backward[idx_i][idx_j][idx_y] = True
                        # Take nums[idx_i], increment idx_j
                        combined_bits = idx_y | nums[idx_i]
                        dp_backward[idx_i][idx_j + 1][combined_bits] = True
                    idx_y += 1
                idx_j += 1

        answer = 0
        scan_index = k
        while scan_index < length_nums - k:
            bit_x = 0
            while bit_x < MAX_BITS:
                if dp_forward[scan_index][k][bit_x]:
                    bit_y = 0
                    while bit_y < MAX_BITS:
                        if dp_backward[scan_index][k][bit_y]:
                            candidate = bit_x ^ bit_y
                            if candidate > answer:
                                answer = candidate
                        bit_y += 1
                bit_x += 1
            scan_index += 1

        return answer