from typing import Callable


def digitSum(param_a: str) -> int:
    if param_a == "":
        return 0

    def helperFunc(param_b: int, param_c: int) -> int:
        if param_b == len(param_a):
            return param_c
        ch = param_a[param_b]
        if not (ch < "A" or ch > "Z"):  # char is in uppercase A-Z range
            return helperFunc(param_b + 1, param_c + ord(ch))
        else:
            return helperFunc(param_b + 1, param_c + 0)

    return helperFunc(1, 0)