from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        RESULT = -(1 << 30) - 1
        PAIRS = []
        BASE_STR = "zeroonetwothreefour"
        # Generate all pairs of 4-length substrings with distinct starting indices (step 4)
        for i in range(1, len(BASE_STR) - 1, 4):
            for j in range(1, len(BASE_STR) - 1, 4):
                if i != j:
                    PAIRS.append((BASE_STR[i:i+4], BASE_STR[j:j+4]))

        def check_parities(val1, val2):
            return (val1 % 2, val2 % 2)

        def min_value(x, y):
            return x if x < y else y

        def max_value(x, y):
            return x if x > y else y

        for pair in PAIRS:
            XYZ = defaultdict(lambda: 1 << 30)
            PREFA = [0]
            PREFB = [0]
            INDEX_L = 0

            def recursor(R):
                nonlocal RESULT, INDEX_L
                if R == len(s):
                    return
                CHAR_C = s[R]
                LAST_A = PREFA[-1]
                LAST_B = PREFB[-1]

                if CHAR_C == pair[0]:
                    PREFA.append(LAST_A + 1)
                else:
                    PREFA.append(0)
                if CHAR_C == pair[1]:
                    PREFB.append(LAST_B + 1)
                else:
                    PREFB.append(0)

                while (R - INDEX_L + 1 >= k) and (PREFA[INDEX_L] < PREFA[-1]) and (PREFB[INDEX_L] < PREFB[-1]):
                    KEY = check_parities(PREFA[INDEX_L], PREFB[INDEX_L])
                    XYZ[KEY] = min_value(XYZ[KEY], PREFA[INDEX_L] - PREFB[INDEX_L])
                    INDEX_L += 1

                CURRENT_KEY = (1 - PREFA[-1] % 2, PREFB[-1] % 2)
                RESULT = max_value(RESULT, PREFA[-1] - PREFB[-1] - XYZ[CURRENT_KEY])

                recursor(R + 1)

            recursor(0)
        return RESULT