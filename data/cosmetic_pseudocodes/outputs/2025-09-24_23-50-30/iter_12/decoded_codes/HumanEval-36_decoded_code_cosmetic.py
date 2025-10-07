from typing import List


def fizz_buzz(integer_n: int) -> int:
    beta: int = 0
    gamma: str = ""
    delta: List[int] = []

    def helper(alpha: int) -> None:
        if alpha == integer_n:
            return
        else:
            # Check if alpha is divisible by 11 or 13
            if alpha % 11 == 0 or alpha % 13 == 0:
                delta.append(alpha)
            helper(alpha + 1)

    helper(0)

    gamma = "".join(str(x) for x in delta)

    for phi in gamma:
        if phi == "7":
            beta += 1

    return beta