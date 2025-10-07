from typing import List, Dict, Tuple

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def helper(A: int, B: int, C: int, D: int) -> int:
            def internal(X: int, Y: int, Z: int, W: Dict[Tuple[int, int, int], int]) -> int:
                if not (X < Y):
                    return 0

                key = (X, Y, Z)
                if key in W:
                    return W[key]

                res = 0
                R_val_2 = nums[X]
                R_val_3 = nums[X + 1]
                R_val_4 = nums[Y]
                R_val_5 = nums[Y - 1]

                SUM1 = R_val_2 + R_val_3
                SUM2 = R_val_5 + R_val_4
                SUM3 = R_val_2 + R_val_4

                if SUM1 == Z:
                    tmp = 1 + internal(X + 2, Y, Z, W)
                    if tmp > res:
                        res = tmp

                if SUM2 == Z:
                    tmp = 1 + internal(X, Y - 2, Z, W)
                    if tmp > res:
                        res = tmp

                if SUM3 == Z:
                    tmp = 1 + internal(X + 1, Y - 1, Z, W)
                    if tmp > res:
                        res = tmp

                W[key] = res
                return res

            LEN = A
            RESULT_1 = 1 + internal(2, LEN - 1, B, {})
            RESULT_2 = 1 + internal(0, LEN - 3, C, {})
            RESULT_3 = 1 + internal(1, LEN - 2, D, {})
            TMP_RESULTS = [RESULT_1, RESULT_2, RESULT_3]
            FINAL_RESULT = TMP_RESULTS[0]
            INDEX_TMP = 1
            while INDEX_TMP < 3:
                if TMP_RESULTS[INDEX_TMP] > FINAL_RESULT:
                    FINAL_RESULT = TMP_RESULTS[INDEX_TMP]
                INDEX_TMP += 1

            return FINAL_RESULT

        L_num = len(nums)
        SCORE_1 = nums[0] + nums[1]
        SCORE_2 = nums[L_num - 2] + nums[L_num - 1]
        SCORE_3 = nums[0] + nums[L_num - 1]

        return helper(L_num, SCORE_1, SCORE_2, SCORE_3)