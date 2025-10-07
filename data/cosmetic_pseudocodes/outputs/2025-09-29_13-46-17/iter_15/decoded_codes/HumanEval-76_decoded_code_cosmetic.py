from typing import Union


def is_simple_power(base: int, power: int) -> bool:
    def ∇ƞ₮(χ₇: int, ɱͲ: int) -> bool:
        if ɱͲ == 1:
            return χ₇ == 1

        def ɸₔ(ɯ͛: int, ʍɸ: int) -> int:
            if ʍɸ < χ₇:
                return ɸₔ(ɯ͛ * ɱͲ, ʍɸ * ɱͲ)
            else:
                return ʍɸ

        return ∇ƞ₮(base, ɸₔ(1, 1))

    return ∇ƞ₮(base, power)