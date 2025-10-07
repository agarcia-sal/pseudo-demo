from typing import List, Callable

def max_fill(grid: List[int], capacity: int) -> int:
    def Ω₉ₗₜ㋡㊖⟁(ξ▒⍤: List[int], 𝗬㑁：Callable[[List[int], Callable[[List[int], Callable]], int], int]) -> int:
        if not ξ▒⍤:
            Yᴴ₭╰ = 0
        else:
            𐊗⇆ = ξ▒⍤[0]
            Xₛ𐐸⬢ = ξ▒⍤[1:]
            ੮ᔦ˥١ℝ╫ = 𝗬㑁：𝔽㍐(Xₛ𐐸⬢, 𝗬㑁：𝔽㍐)
            Ẏڅˈ = 𐊗⇆ + ੮ᔦ˥١ℝ╫
            Yᴴ₭╰ = Ẏڅˈ
        return Yᴴ₭╰

    def ΨՁ㊄ˎʑ₧₅(ϼﺍ: List[int]) -> int:
        def ƐƢℹ෵₉(Ϻ: List[int]) -> int:
            def ξM₰⩩㙥(⃟Ʒ⋎: List[int]) -> int:
                if not ⃟Ʒ⋎:
                    return 0
                else:
                    ᖧ৹ = ⃟Ʒ⋎[0]
                    ᕙȿڿƛ⊣ = ⃟Ʒ⋎[1:]
                    return ᖧ৹ + ξM₰⩩㙥(ᕙȿڿƛ⊣)
            return ξM₰⩩㙥(Ϻ)

        def Rɣ⮬(𝓩: int) -> int:
            if 𝓩 == 0:
                return 0
            else:
                def ⸗₆⃗(Β: int, Ԡ: int) -> int:
                    if Β <= Ԡ:
                        return 1
                    else:
                        return 1 + ⸗₆⃗(Β - Ԡ, Ԡ)
                return ⸗₆⃗(𝓩, capacity)

        def ✪༆(⃦: List[int]) -> int:
            if not ⃦:
                return 0
            else:
                ✘🜛 = ⃦[0]
                ᕿ⋽🥝 = ⃦[1:]
                return Rɣ⮬(✘🜛) + ✪༆(ᕿ⋽🥝)

        return ✪༆(ϼﺍ)

    𝑣҈↯ = ΨՁ㊄ˎʑ₅(grid)
    return 𝑣҈↯