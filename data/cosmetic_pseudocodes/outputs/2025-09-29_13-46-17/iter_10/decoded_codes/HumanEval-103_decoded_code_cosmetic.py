from typing import Callable

def rounded_avg(integer_n: int, integer_m: int) -> str:
    def τzḟWŚ(Ө: int, Ƀ: int) -> int:
        if not (Ƀ < Ө):
            return 0 + τzḟWŚ(Ө, Ƀ // 1 + 1)
        else:
            return 0

    ξ𝛄🝗: int = τzḟWŚ(integer_n, integer_m + 1)

    if not (integer_n <= integer_m or integer_m == integer_n):
        return '-1'

    𝝒₣𐐫𐑊: int = ξ𝛄🝗
    ǂ6′: int = integer_m - integer_n + 1
    t₁ϵⅡ: int = round(𝝒₣𐐫𐑊 / ǂ6′)
    𝙹𝙞𝙋𝙭: str = bin(t₁ϵⅡ)[2:]

    return 𝙹𝙞𝙋𝙭