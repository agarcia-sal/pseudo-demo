class Solution:
    def countOfPairs(self, nums):
        CONST_MOD = 10**9 + 7
        LEN_ARR = len(nums)
        MAX_ELEMENT = max(nums)

        # Initialize 3D DP table with zeros
        TABLE = [[[0] * (MAX_ELEMENT + 1) for _ in range(MAX_ELEMENT + 1)] for __ in range(LEN_ARR + 1)]

        IDX0_NUM = nums[0]
        for X000 in range(IDX0_NUM + 1):
            TABLE[1][X000][IDX0_NUM - X000] = 1

        POS = 2
        while POS <= LEN_ARR:
            CUR_NUM = nums[POS - 1]
            for AAA in range(CUR_NUM + 1):
                for BBB in range(CUR_NUM + 1):
                    if AAA + BBB == CUR_NUM:
                        for P in range(AAA + 1):
                            Q = BBB
                            while Q <= MAX_ELEMENT:
                                TABLE[POS][AAA][BBB] = (TABLE[POS][AAA][BBB] + TABLE[POS - 1][P][Q]) % CONST_MOD
                                Q += 1
            POS += 1

        FINAL_RESULT = 0
        for JJ in range(MAX_ELEMENT + 1):
            for KK in range(MAX_ELEMENT + 1):
                FINAL_RESULT = (FINAL_RESULT + TABLE[LEN_ARR][JJ][KK]) % CONST_MOD

        return FINAL_RESULT