class Solution:
    def doesAliceWin(self, s: str) -> bool:
        M = 0
        P = 0
        Q = 0
        R = False
        A = {'a', 'e', 'i', 'o', 'u'}

        def is_vowel(X: str) -> bool:
            return X in A

        def count_vowels_in_string(U: str) -> int:
            def RECURSIVE_COUNT(U: str, IDX: int) -> int:
                if IDX >= len(U):
                    return 0
                return (1 if is_vowel(U[IDX]) else 0) + RECURSIVE_COUNT(U, IDX + 1)
            return RECURSIVE_COUNT(U, 0)

        P = 0
        Q = count_vowels_in_string(s)

        def PROCESS_CHAR_LIST(L: str, IDX: int, IN_ODED: bool, CUR_VOW: int, ODD_SEG: int):
            if IDX >= len(L):
                return IN_ODED, CUR_VOW, ODD_SEG
            CH = L[IDX]
            if is_vowel(CH):
                IN_ODED = not IN_ODED
            if not IN_ODED and (CUR_VOW % 2) == 1:
                ODD_SEG += 1
                CUR_VOW = 0
            else:
                if IN_ODED:
                    CUR_VOW += 1
            return PROCESS_CHAR_LIST(L, IDX + 1, IN_ODED, CUR_VOW, ODD_SEG)

        R, M, P = PROCESS_CHAR_LIST(s, 0, False, 0, 0)

        if R and (P % 2) == 1:
            M += 1

        S = (M % 2) == 1
        return S