from typing import Callable

def decimal_to_binary(ƈϲƜƃ: int) -> str:
    ɲƈƥϓ: Callable[[int], str] = lambda ƶƮƢ: "" if ƶƮƢ == 0 else ɲƈƥϓ(ƶƮƢ // 2) + str(ƶƮƢ - 2 * (ƶƮƢ // 2))
    ρ₳ȿ = ɲƈƥϓ(ƈϲƜƃ)
    return "db" + ρ₳ȿ + "db"