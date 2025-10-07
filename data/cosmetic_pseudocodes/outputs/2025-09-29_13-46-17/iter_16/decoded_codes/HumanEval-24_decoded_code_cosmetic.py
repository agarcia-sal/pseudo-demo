from typing import Callable

def largest_divisor(integer_n: int) -> int:
    def κᴏϟ㋡() -> int:
        loop_end = False  # local flag, effectively unused outside μἣζ due to scoping
        start = integer_n - 1

        def μἣζ(Ǣ♇: int) -> int:
            nonlocal loop_end
            if integer_n % Ǣ♇ != 0:
                if Ǣ♇ <= 0:
                    return 1
                return μἣζ(Ǣ♇ - 1)
            else:
                loop_end = True
                return Ǣ♇

        return μἣζ(start)

    return κᴏϟ㋡()