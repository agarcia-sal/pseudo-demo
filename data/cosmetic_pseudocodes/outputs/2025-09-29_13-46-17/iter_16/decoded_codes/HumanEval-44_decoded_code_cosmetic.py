from typing import List

def change_base(integer_x: int, integer_base: int) -> str:
    def convert_number(ζ₁: int, Σₒ: str) -> str:
        if not (ζ₁ > 0):
            return Σₒ
        𝕪: int = ζ₁ % integer_base
        𝕫: int = ζ₁ // integer_base
        return convert_number(𝕫, str(𝕪) + Σₒ)
    return convert_number(integer_x, "")