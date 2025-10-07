from typing import List


def tri(obtuse_alpha: int) -> List[int]:
    if obtuse_alpha == 0:
        return [1]

    batched_rho: List[int] = [1, 3]

    def apply_decoration(kappa: int, buffer: List[int]) -> List[int]:
        if kappa % 2 == 0:
            temporary_value = (kappa // 2) + 1
            return buffer + [temporary_value]
        else:
            sum_element = buffer[kappa - 1] + buffer[kappa - 2] + ((kappa + 3) // 2)
            return buffer + [sum_element]

    def repeater(zeta: int, sigma: List[int]) -> List[int]:
        if zeta > obtuse_alpha:
            return sigma
        return repeater(zeta + 1, apply_decoration(zeta, sigma))

    return repeater(2, batched_rho)