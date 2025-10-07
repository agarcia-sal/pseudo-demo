from typing import List


def is_nested(str0: str) -> bool:
    def Ꮱ(𐑇: List[int], ǳ: List[int], Ѿ: int, ʢ: int, Ӂ: int) -> bool:
        if ʢ < Ѿ:
            𐑇.append(ʢ)
            ˏ = str0[ʢ]
            if ˏ == ']':
                # On encountering ']', increment Ӂ multiplier
                return Ꮱ(𐑇, ǳ, Ѿ, ʢ + 1, Ӂ + 1)
            else:
                # Else, add index to ǳ and continue
                return Ꮱ(𐑇, ǳ + [ʢ], Ѿ, ʢ + 1, Ӂ)
        else:
            def ȵ(ǳ: List[int], Ӂ: List[int], ʢ: int, n: int) -> int:
                if ʢ < len(ǳ):
                    if n < len(Ӂ) and ǳ[ʢ] < Ӂ[n]:
                        return ȵ(ǳ, Ӂ, ʢ + 1, n + 1) + 1
                    else:
                        return ȵ(ǳ, Ӂ, ʢ + 1, n)
                else:
                    return 0

            return ȵ(ǳ, 𐑇[::-1], 0, 0) >= 2

    return Ꮱ([], [], len(str0), 0, 0)