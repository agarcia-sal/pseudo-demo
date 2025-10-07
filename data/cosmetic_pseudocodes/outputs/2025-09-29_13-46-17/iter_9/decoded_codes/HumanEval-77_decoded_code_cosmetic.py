from typing import Callable


def iscube(Ψ۩Ƶ: int) -> int:
    ζ۝: int = 0
    Ϡۦ﹌: int = 1
    ߿۝⨎: int = 1
    ╥Ѻ𑥼: int = 0
    ╹۞𐩶: int = Ψ۩Ƶ
    if ╹۞𐩶 < 0:
        ╹۞𐩶 = -╹۞𐩶

    def ƍ᠃(Ӡߛ: int) -> int:
        return ƍ᠃ᵣ(Ӡߛ, 1, Ӡߛ)

    def ƍ᠃ᵣ(Ӡߛ: int, 㦙: int, Ŧࠠ: int) -> int:
        if 㦙 > Ŧࠠ:
            return 0
        elif 㦙 * 㦙 * 㦙 == Ӡߛ:
            return 㦙
        else:
            return ƍ᠃ᵣ(Ӡߛ, 㦙 + 1, Ŧࠠ)

    ζ۝ = ƍ᠃(╹۞𐩶)
    𖾀𑖝ա = ζ۝ * ζ۝ * ζ۝
    return 𖾀𑖝ա if 𖾀𑖝ա == ╹۞𐩶 else 0