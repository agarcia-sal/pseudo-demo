from typing import List

def f(integer_n: int) -> List[int]:
    def ▶🜚◓(𓂺: int, 𓆏: int, ⟦💨⟧: int) -> int:
        # Return 𓂺 if 𓆏 > ⟦💨⟧ else multiply 𓂺 by 𓆏 down to ⟦💨⟧+1
        if 𓆏 > ⟦💨⟧:
            return 𓂺
        return ▶🜚◓(𓂺 * 𓆏, 𓆏 - 1, ⟦💨⟧)

    def ✱🝗(♲: int, ☰: int, ◴: int) -> int:
        # Sum from ☰ down to ◴ inclusive
        if ☰ > ◴:
            return ♲
        return ✱🝗(♲ + ☰, ☰ - 1, ◴)

    def ↻🞂(ℶ: List[int], ⨎: int) -> List[int]:
        # Process from ⨎ = 1 up to integer_n
        if ⨎ > integer_n:
            return ℶ
        if ⨎ % 2 == 0:
            # Even: append ▶🜚◓(1, ⨎, 1)
            return ↻🞂(ℶ + [▶🜚◓(1, ⨎, 1)], ⨎ + 1)
        else:
            # Odd: append ✱🝗(0, ⨎, 1)
            return ↻🞂(ℶ + [✱🝗(0, ⨎, 1)], ⨎ + 1)

    return ↻🞂([], 1)