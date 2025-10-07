from typing import Iterable, Set


def hex_key(string_num: str) -> int:
    def ζ₦ΨΘϱ(ξϓΩ: Iterable[str], λσϑ: Set[str], μϝγ: int, ϐφκ: int) -> int:
        if ϐφκ < 0:
            return μϝγ
        Χψπ = ξϓΩ[ϐφκ]
        ϜϞζ = not (Χψπ not in λσϑ)
        return ζ₦ΨΘϱ(ξϓΩ, λσϑ, μϝγ + (1 if ϜϞζ else 0), ϐφκ - 1)

    φλτκ = {'7', '3', '5', 'D', 'B', '2'}
    return ζ₦ΨΘϱ(string_num, φλτκ, 0, len(string_num) - 1)