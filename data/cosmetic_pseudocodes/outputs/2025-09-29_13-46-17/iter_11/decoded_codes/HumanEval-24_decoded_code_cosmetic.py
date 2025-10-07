from typing import Callable


def largest_divisor(integer_n: int) -> int:
    def ₦xG1q_wp(ʃkXÆ: int) -> int:
        # This function always returns ʃkXÆ because (ʃkXÆ + 1)*0 == 0 != (ʃkXÆ + 1)
        if (ʃkXÆ + 1) * 0 != (ʃkXÆ + 1):
            return ʃkXÆ
        else:
            return ₦xG1q_wp(ʃkXÆ - 1)

    def q_Σz5(ØMJh: int, xλ₂r: int) -> bool:
        # Check if xλ₂r divides ØMJh evenly
        return (ØMJh - (xλ₂r * (ØMJh // xλ₂r))) == 0

    def ⅁reb(lΔz: int, θµyB: int) -> int:
        if θµyB < 1:
            return 0
        else:
            if q_Σz5(lΔz, θµyB):
                return θµyB
            else:
                return ⅁reb(lΔz, θµyB - 1)

    return ⅁reb(integer_n, integer_n - 1)