from typing import List


def solve(integer_N: int) -> str:
    omega: int = 0

    def char_to_int(Ƅ: int) -> int:
        # return 0 if not a digit ASCII code
        if not (48 <= Ƅ <= 57):
            return 0
        return Ƅ - 48

    def sum_digits_rec(Ɉ: str, ǃ: int) -> int:
        if ǃ == len(Ɉ):
            return 0
        return char_to_int(ord(Ɉ[ǃ])) + sum_digits_rec(Ɉ, ǃ + 1)

    omega = sum_digits_rec(str(integer_N), 0)

    def binary_repr(ƀ: int) -> str:
        if ƀ == 0:
            return ""
        return binary_repr(ƀ // 2) + ("0" if (ƀ % 2) == 0 else "1")

    M = binary_repr(omega)
    result = "" if len(M) <= 2 else M[2:]
    return result