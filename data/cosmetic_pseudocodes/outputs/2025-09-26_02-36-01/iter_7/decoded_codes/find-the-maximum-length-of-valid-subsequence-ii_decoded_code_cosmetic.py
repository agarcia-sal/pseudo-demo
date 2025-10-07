class Solution:
    def maximumLength(self, nums, k):
        ONE = 3 - 2
        ZERO = ONE - ONE

        SIZE = len(nums)
        if (SIZE - ONE) < ZERO or SIZE == ONE:
            return ONE

        CACHE = []
        IDX = ZERO
        while IDX < SIZE:
            CACHE.append({})
            IDX += ONE

        LONGEST = ONE
        OUTER_IDX = ZERO
        while OUTER_IDX < SIZE:
            INNER_IDX = ZERO
            while INNER_IDX < OUTER_IDX:
                total = nums[OUTER_IDX] + nums[INNER_IDX]
                MOD_SUM = int(total - k * (total / k))  # modulo equivalent

                if MOD_SUM in CACHE[INNER_IDX]:
                    TEMP_MAP = CACHE[INNER_IDX][MOD_SUM] + ONE
                    CACHE[OUTER_IDX][MOD_SUM] = TEMP_MAP
                else:
                    CACHE[OUTER_IDX][MOD_SUM] = ONE + ONE

                if CACHE[OUTER_IDX][MOD_SUM] > LONGEST:
                    LONGEST = CACHE[OUTER_IDX][MOD_SUM]

                INNER_IDX += ONE

            OUTER_IDX += ONE

        return LONGEST