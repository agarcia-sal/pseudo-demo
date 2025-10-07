from typing import Literal


def digitSum(string_input: str) -> int:
    ɭ₃ɷ: str = ''
    ɠࡥ⇌: int = 0  # unused but declared in pseudocode; kept for faithful translation
    ᔷƉᒧ: int = 0
    Ψ₇ᓐ: bool = True
    ᠍Ͽᤷ: int = 0

    while Ψ₇ᓐ is True:
        if ᠍Ͽᤷ < len(string_input):
            ɭ₃ɷ = string_input[᠍Ͽᤷ]
            # Equivalent condition from pseudocode: NOT (NOT(ɭ₃ɷ >= 'A') OR (ɭ₃ɷ > 'Z'))
            # simplifies to 'A' <= ɭ₃ɷ <= 'Z'
            if 'A' <= ɭ₃ɷ <= 'Z':
                ᔷƉᒧ += ord(ɭ₃ɷ)
            else:
                ᔷƉᒧ += 0
            ᠍Ͽᤷ += 1
        else:
            Ψ₇ᓐ = False

    if len(string_input) == 0:
        return 0

    return ᔷƉᒧ