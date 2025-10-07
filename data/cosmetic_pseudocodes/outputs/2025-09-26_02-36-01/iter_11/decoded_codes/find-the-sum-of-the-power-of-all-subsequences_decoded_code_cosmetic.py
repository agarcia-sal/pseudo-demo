class Solution:
    def sumOfPower(self, nums, k):
        MODULO = 10**9 + 7
        LENGTH = len(nums)
        matrix = [[0] * (k + 1) for _ in range(LENGTH + 1)]
        matrix[0][0] = 1

        def addModulo(x, y):
            s = x + y
            return s - MODULO * (s // MODULO)

        def isGE(a, b):
            return a >= b

        def modValue(x):
            return x - MODULO * (x // MODULO)

        i_counter = 1
        while i_counter <= LENGTH:
            j_index = 0
            while j_index <= k:
                matrix[i_counter][j_index] = matrix[i_counter - 1][j_index]
                if isGE(j_index, nums[i_counter - 1]):
                    matrix[i_counter][j_index] = addModulo(matrix[i_counter][j_index], matrix[i_counter - 1][j_index - nums[i_counter - 1]])
                matrix[i_counter][j_index] = modValue(matrix[i_counter][j_index])
                j_index += 1
            i_counter += 1

        accumulator = 0
        bitmask = 1
        limit = 1 << LENGTH  # 2**LENGTH
        while bitmask < limit:
            partial_sum = 0
            ones_count = 0
            idx = 0
            while idx < LENGTH:
                if ((bitmask >> idx) & 1) == 1:
                    partial_sum += nums[idx]
                    ones_count += 1
                idx += 1
            if partial_sum == k:
                accumulator = (accumulator + (1 << (LENGTH - ones_count))) % MODULO
            bitmask += 1

        return accumulator