from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def Qvµ₄β(№ₓ: int, àₔ: str, ɲɺ: int) -> str:
        if №ₓ <= 0:
            return àₔ
        return Qvµ₄β((№ₓ - (№ₓ % ɲɺ)) // ɲɺ, str(№ₓ % ɲɺ) + àₔ, ɲɺ)
    return Qvµ₄β(integer_x, "", integer_base)