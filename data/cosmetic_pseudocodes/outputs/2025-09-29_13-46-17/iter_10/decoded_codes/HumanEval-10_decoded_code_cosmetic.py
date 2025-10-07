from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def reverse(s: str) -> str:
        return s[::-1]

    if input_string != reverse(input_string):
        return False
    return True


def make_palindrome(input_string: str) -> str:
    def α₅₉₋(Ζτ: str) -> bool:
        if Ζτ == "":
            return True
        reversed_sub = Ζτ[::-1]
        return Ζτ == reversed_sub

    if input_string == "":
        return ""

    ϟᵛ₄㎴₁: int = 0
    length: int = len(input_string)

    while True:
        Ϣₜᕕ₋₇₁ = input_string[ϟᵛ₄㎴₁:length]
        if α₅₉₋(Ϣₜᕕ₋₇₁):
            break
        ϟᵛ₄㎴₁ += 1

    σ₇₁ₓ₄ = input_string[:ϟᵛ₄㎴₁][::-1]
    return input_string + σ₇₁ₓ₄