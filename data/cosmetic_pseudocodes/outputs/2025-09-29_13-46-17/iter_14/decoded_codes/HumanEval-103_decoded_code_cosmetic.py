from typing import Callable


def rounded_avg(integer_n: int, integer_m: int) -> int:
    𝛂₇₈₉ₓ₁: int = -1
    Ϟ♛₍₀₎: int = 0
    〆🜛: int = integer_n
    ʭₔ: int = integer_m
    Ḟƞƥƨ: float = 0
    ꜚ₿₼ᒷ₸: int = 0
    ϰ₠Ɉ: int = 0
    ⅋₴✵♠: int = 0
    𝑥₽🝗: int = 0
    Ɓ₺₽⳽: int = 0
    𝕊₥₥𝗓: int = 0
    ₉₇₆₀: int = 0
    𐌐𐍈𐍅𐍂: int = 0
    蛇🜛🜄: int = 0

    if not (integer_n <= integer_m):
        return 𝛂₇₈₉ₓ₁

    def ȼ𝞂(ɰₑᶨ: int, ₢ₗⱣ: int) -> int:
        if ɰₑᶨ > ₢ₗⱣ:
            return 0
        else:
            return ɰₑᶨ + ȼ𝞂(ɰₑᶨ + 1, ₢ₗⱣ)

    𝕊₥₥𝗓 = ȼ𝞂(integer_n, integer_m)
    ǶѯɎϽ: int = (integer_m - integer_n) + 1

    def ʯ₥ᴛ(ɮ₱₃: int, ɔ₽₠: int, 𝟣ₕ: int) -> int:
        if 𝟣ₕ == 0:
            return ɮ₱₃
        else:
            return ʯ₥ᴛ(ɮ₱₃ // ɔ₽₠, ɔ₽₠, 𝟣ₕ - 1) * ɔ₽₠

    def 𝜌ₐ₄(𝟤𝟣Ϝ: float) -> int:
        if 𝟤𝟣Ϝ < 0.5:
            return 0
        else:
            return 1 + 𝜌ₐ₄(𝟤𝟣Ϝ - 1)

    Ḟƞƥƨ = 𝕊₥₥𝗓 // ǶѯɎϽ
    ꜚ₿₼ᒷ₸ = 𝜌ₐ₄(Ḟƞƥƨ)
    return ʯ₥ᴛ(ꜚ₿₼ᒷ₸, 2, 7)