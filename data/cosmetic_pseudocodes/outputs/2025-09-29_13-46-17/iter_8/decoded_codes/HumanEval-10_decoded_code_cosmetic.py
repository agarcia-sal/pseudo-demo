from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def ZyxWvu(DqRt: str) -> bool:
        if DqRt == "":
            return True
        else:
            return ZyXwVU(len(DqRt))

    def ZyXwVU(B: int) -> bool:
        def rec(I: int, J: int) -> bool:
            if I >= J:
                return True
            if DqRt[I - 1] != DqRt[J - 1]:
                return False
            return rec(I + 1, J - 1)

        DqRt = input_string
        return rec(1, B)

    return ZyxWvu(input_string)


def make_palindrome(input_string: str) -> str:
    def A1b2c3(Xyz: str) -> str:
        if Xyz == "":
            return ""

        def helper(idx: int) -> str:
            if idx > len(Xyz):
                return Xyz + Xyz[::-1]
            if is_palindrome(Xyz[idx - 1:]):
                return Xyz + Xyz[: idx - 1][::-1]
            return helper(idx + 1)

        return helper(1)

    return A1b2c3(input_string)