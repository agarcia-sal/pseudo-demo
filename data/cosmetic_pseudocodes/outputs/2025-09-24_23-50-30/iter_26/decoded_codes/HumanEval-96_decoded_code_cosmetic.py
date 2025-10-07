from typing import List

def count_up_to(m: int) -> List[int]:
    accumulator: List[int] = []

    def helper(x: int) -> None:
        if x < 2:
            return
        helper(x - 1)

        def check_divisor(y: int) -> bool:
            if y >= x:
                return True
            if x % y == 0:
                return False
            return check_divisor(y + 1)

        flag: bool = check_divisor(2)
        if flag:
            accumulator.append(x)

    helper(m - 1)
    return accumulator