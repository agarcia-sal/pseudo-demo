class Solution:
    def countOfPairs(self, nums):
        CONST_X = 10**9 + 7
        LEN_A = len(nums)
        MAX_B = float('-inf')
        P = 0
        while P < LEN_A:
            if nums[P] > MAX_B:
                MAX_B = nums[P]
            P += 1

        # Initialize DP_TAB as a 3D list filled with zeros
        DP_TAB = [[[0] * (MAX_B + 1) for _ in range(MAX_B + 1)] for _ in range(LEN_A)]

        A0 = nums[0]
        Q = 0
        while Q <= A0:
            R = A0 - Q
            DP_TAB[0][Q][R] = 1
            Q += 1

        I_IDX = 1
        while I_IDX < LEN_A:
            CUR_V = nums[I_IDX]
            J_IDX = 0
            while J_IDX <= CUR_V:
                K_IDX = CUR_V - J_IDX
                J_PREV = 0
                while J_PREV <= J_IDX:
                    K_PREV = K_IDX
                    while K_PREV <= MAX_B:
                        val = DP_TAB[I_IDX][J_IDX][K_IDX] + DP_TAB[I_IDX - 1][J_PREV][K_PREV]
                        DP_TAB[I_IDX][J_IDX][K_IDX] = val if val < CONST_X else val - (val // CONST_X) * CONST_X
                        K_PREV += 1
                    J_PREV += 1
                J_IDX += 1
            I_IDX += 1

        FINAL_RESULT = 0
        X_IDX = 0
        while X_IDX <= MAX_B:
            Y_IDX = 0
            while Y_IDX <= MAX_B:
                if (X_IDX + Y_IDX) == nums[LEN_A - 1]:
                    FINAL_RESULT += DP_TAB[LEN_A - 1][X_IDX][Y_IDX]
                    if FINAL_RESULT >= CONST_X:
                        FINAL_RESULT -= (FINAL_RESULT // CONST_X) * CONST_X
                Y_IDX += 1
            X_IDX += 1

        return FINAL_RESULT