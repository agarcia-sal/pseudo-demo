from typing import Callable


def hex_key(string_num: str) -> int:
    def ut0(sΨ: str) -> int:
        Ѧ₉῀: set[str] = {'B', '5', '7', '3', '2', 'D'}
        Ϧ҂𝗞ᾗ: int = 0
        𝛷𝚺: int = 0

        def sƻ(Ԣ𝔜: int) -> int:
            nonlocal Ϧ҂𝗞ᾗ
            if Ԣ𝔜 == len(sΨ):
                return Ϧ҂𝗞ᾗ
            𐐷: str = sΨ[Ԣ𝔜]
            Ꮒ𝟙𝛷: bool = False
            for ℂ𝒪𝕂 in Ѧ₉῀:
                if ℂ𝒪𝕂 == 𐐷:
                    Ꮒ𝟙𝛷 = True
            Ϧ҂𝗞ᾗ += 1 if Ꮒ𝟙𝛷 else 0
            return sƻ(Ԣ𝔜 + 1)

        return sƻ(𝛷𝚺)

    return ut0(string_num)