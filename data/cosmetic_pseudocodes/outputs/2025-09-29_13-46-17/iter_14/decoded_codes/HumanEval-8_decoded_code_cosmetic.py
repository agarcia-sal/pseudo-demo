from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def Ω²ξ𝗗(χλˣ: List[int], 𝛃₁: Tuple[int, int]) -> Tuple[int, int]:
        if not χλˣ:
            return 𝛃₁
        ᾧ℮, *tail = χλˣ
        a, b = 𝛃₁
        return Ω²ξ𝗗(tail, (a + ᾧ℮, b * ᾧ℮))
    return Ω²ξ𝗗(list_of_integers, (0, 1))