class Solution:
    def countOfPairs(self, nums):
        modulus = 10 ** 9 + 7
        length_nums = len(nums)

        def findMax(arr, idx, currentMax):
            if idx == len(arr):
                return currentMax
            else:
                if arr[idx] > currentMax:
                    return findMax(arr, idx + 1, arr[idx])
                else:
                    return findMax(arr, idx + 1, currentMax)

        highest = findMax(nums, 0, 0)

        def create1DArray(size):
            if size == 0:
                return []
            else:
                return [0] + create1DArray(size - 1)

        def create2DArray(a, b):
            if a == 0:
                return []
            else:
                row = create1DArray(b)
                remaining = create2DArray(a - 1, b)
                return [row] + remaining

        def create3DArray(x, y, z):
            if x == 0:
                return []
            else:
                layer = create2DArray(y, z)
                rest = create3DArray(x - 1, y, z)
                return [layer] + rest

        matrix_dp = create3DArray(length_nums, highest + 1, highest + 1)

        # Since the pseudocode's setValue3D copies entire array but updates only one element,
        # to maintain correctness and efficiency, we'll mutate in place as standard Python lists allow it.
        def setValue3D(arr, i, j, k, val):
            arr[i][j][k] = val
            return arr

        def getValue3D(arr, i, j, k):
            return arr[i][j][k]

        firstNum = nums[0]

        def assignInitialDP(index, val):
            if index > val:
                return matrix_dp
            else:
                part_k = val - index
                setValue3D(matrix_dp, 0, index, part_k, 1)
                return assignInitialDP(index + 1, val)

        dp_after_init = assignInitialDP(0, firstNum)

        def innerMostLoop(i, j, j_prev_loop, k, max_val_loop, dp_current):
            if k > max_val_loop:
                return dp_current
            else:
                current = getValue3D(dp_current, i, j, k)
                prev_val = getValue3D(dp_current, i - 1, j_prev_loop, k)
                sum_val = (current + prev_val) % modulus
                setValue3D(dp_current, i, j, k, sum_val)
                return innerMostLoop(i, j, j_prev_loop, k + 1, max_val_loop, dp_current)

        def innerLoopJPrev(i, j, j_prev_val, k, max_value, dp_current):
            if j_prev_val > j:
                return dp_current
            else:
                dp_after_innermost = innerMostLoop(i, j, j_prev_val, k, max_value, dp_current)
                return innerLoopJPrev(i, j, j_prev_val + 1, k, max_value, dp_after_innermost)

        def innerLoopJK(i, j, k_val, max_value, dp_current):
            if k_val > max_value:
                return dp_current
            else:
                dp_after_jprev = innerLoopJPrev(i, j, 0, k_val, max_value, dp_current)
                return innerLoopJK(i, j, k_val + 1, max_value, dp_after_jprev)

        def loopOverJ(i, j_val, num_i, max_value, dp_current):
            if j_val > num_i:
                return dp_current
            else:
                dp_after_inner = innerLoopJK(i, j_val, 0, max_value, dp_current)
                return loopOverJ(i, j_val + 1, num_i, max_value, dp_after_inner)

        def loopI(i_val, limit_n, nums_arr, max_value, dp_current):
            if i_val > limit_n:
                return dp_current
            else:
                num_at_i = nums_arr[i_val]
                dp_after_jloop = loopOverJ(i_val, 0, num_at_i, max_value, dp_current)
                return loopI(i_val + 1, limit_n, nums_arr, max_value, dp_after_jloop)

        dp_full = loopI(1, length_nums - 1, nums, highest, dp_after_init)

        def computeResult(j_val, k_val, max_val, last_num, dp_arr, accum):
            if j_val > max_val:
                return accum
            else:
                if k_val > max_val:
                    return computeResult(j_val + 1, 0, max_val, last_num, dp_arr, accum)
                else:
                    if j_val + k_val == last_num:
                        val = dp_arr[length_nums - 1][j_val][k_val]
                        new_accum = (accum + val) % modulus
                        return computeResult(j_val, k_val + 1, max_val, last_num, dp_arr, new_accum)
                    else:
                        return computeResult(j_val, k_val + 1, max_val, last_num, dp_arr, accum)

        res = computeResult(0, 0, highest, nums[length_nums - 1], dp_full, 0)
        return res