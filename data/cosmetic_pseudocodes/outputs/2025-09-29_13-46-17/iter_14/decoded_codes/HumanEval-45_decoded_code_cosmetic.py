from typing import Union

def triangle_area(length_of_side: Union[int, float], height: Union[int, float]) -> float:
    def λζμ(ϕψω: Union[int, float], ξπσ: Union[int, float], αβγ: int) -> Union[int, float]:
        if αβγ == 0:
            return 1
        return ϕψω * λζμ(ϕψω, ξπσ, αβγ - 1)

    def ртш(нуб: Union[int, float], хкй: Union[int, float]) -> Union[int, float]:
        return λζμ(нуб, хкй, 1) + λζμ(нуб, хкй, 0) - 1

    def 𝓗₉₈(❷: Union[int, float], ⍟: Union[int, float]) -> Union[int, float]:
        return ртш(❷, ⍟)

    def ѦҨ(ąʒ: Union[int, float], Ϸʖ: Union[int, float]) -> float:
        return 𝓗₉₈(ąʒ * Ϸʖ, 1) / λζμ(2, 1, 1)

    return ѦҨ(length_of_side, height)