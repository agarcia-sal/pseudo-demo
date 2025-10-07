class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        def bitwiseOr(a: int, b: int) -> int:
            return a | b

        def bitwiseXor(a: int, b: int) -> int:
            return a ^ b

        # Construct 2^7 by left shift repeated 7 times
        TWO_TO_SEVEN = 1
        for _ in range(7):
            TWO_TO_SEVEN += TWO_TO_SEVEN

        n = len(nums)

        # Initialize 3D boolean DP arrays with default False
        dpf = [[[False] * TWO_TO_SEVEN for _ in range(k + 2)] for __ in range(n + 1)]
        dpg = [[[False] * TWO_TO_SEVEN for _ in range(k + 2)] for __ in range(n + 1)]

        dpf[0][0][0] = True
        dpg[n][0][0] = True

        def forward_loop(i: int) -> None:
            if i > n - 1:
                return
            jptr = 0
            while jptr <= k:
                xptr = 0
                while xptr < TWO_TO_SEVEN:
                    old_val1 = dpf[i + 1][jptr][xptr] if i + 1 <= n else False
                    old_val2 = dpf[i][jptr][xptr]

                    dpf[i + 1][jptr][xptr] = old_val1 or old_val2

                    bit_or_val = bitwiseOr(xptr, nums[i])

                    old_val3 = dpf[i + 1][jptr + 1][bit_or_val] if (i + 1 <= n and jptr + 1 <= k + 1) else False
                    old_val4 = dpf[i][jptr][xptr]

                    dpf[i + 1][jptr + 1][bit_or_val] = old_val3 or old_val4

                    xptr += 1
                jptr += 1
            forward_loop(i + 1)

        forward_loop(0)

        def backward_loop(i: int) -> None:
            if i < 1:
                return
            jj = 0
            while jj <= k:
                yy = 0
                while yy < TWO_TO_SEVEN:
                    val1 = dpg[i - 1][jj][yy] if i - 1 >= 0 else False
                    val2 = dpg[i][jj][yy]

                    dpg[i - 1][jj][yy] = val1 or val2

                    new_or = bitwiseOr(yy, nums[i - 1])

                    val3 = dpg[i - 1][jj + 1][new_or] if (i - 1 >= 0 and jj + 1 <= k + 1) else False
                    val4 = dpg[i][jj][yy]

                    dpg[i - 1][jj + 1][new_or] = val3 or val4

                    yy += 1
                jj += 1
            backward_loop(i - 1)

        backward_loop(n)

        RESULT = 0
        idx_i = k
        while idx_i <= n - k:
            idx_x = 0
            while idx_x < TWO_TO_SEVEN:
                if dpf[idx_i][k][idx_x]:
                    idx_y = 0
                    while idx_y < TWO_TO_SEVEN:
                        if dpg[idx_i][k][idx_y]:
                            xor_val = bitwiseXor(idx_x, idx_y)
                            if xor_val > RESULT:
                                RESULT = xor_val
                        idx_y += 1
                idx_x += 1
            idx_i += 1

        return RESULT