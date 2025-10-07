from typing import List


def count_up_to(alpha: int) -> List[int]:
    def helper(beta: int, gamma: List[int]) -> List[int]:
        if beta >= alpha:
            return gamma

        def check_divisor(delta: int) -> bool:
            if delta >= beta:
                return True
            if beta % delta != 0:
                return check_divisor(delta + 1)
            return False

        if check_divisor(2):
            return helper(beta + 1, gamma + [beta])
        return helper(beta + 1, gamma)

    return helper(2, [])