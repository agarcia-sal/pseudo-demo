from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    def ℵ(β: str) -> Union[List[str], int]:
        if ' ' in β:
            return β.split()
        if ',' in β:
            Ϟ = β.replace(',', ' ')
            return Ϟ.split()

        def ψ(ξ: List[str], υ: int, ζ: int) -> int:
            if ζ == len(ξ):
                return υ
            χ = ξ[ζ]
            υ_prime = υ + 1 if 'a' <= χ <= 'z' and (ord(χ) % 2 == 0) else υ
            return ψ(ξ, υ_prime, ζ + 1)

        return ψ(list(β), 0, 0)

    return ℵ(text)