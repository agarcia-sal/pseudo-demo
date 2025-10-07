from typing import List


def triples_sum_to_zero(alpha: List[int]) -> bool:
    length: int = len(alpha)

    def helper(beta: List[int], gamma: int, delta: int) -> bool:
        if delta == length:
            return False

        def second_loop(epsilon: int) -> bool:
            if epsilon == length:
                return helper(beta, gamma + 1, delta)

            def third_loop(zeta: int) -> bool:
                if zeta == length:
                    return second_loop(epsilon + 1)
                if (beta[gamma] + beta[epsilon] + beta[zeta]) == 0:
                    return True
                return third_loop(zeta + 1)

            return third_loop(epsilon + 1)

        return second_loop(gamma + 1)

    return helper(alpha, 0, 0)