from typing import Callable


def is_happy(string_input: str) -> bool:
    def ʎɹɐƃɹnƎ(λ: int, ξ: int, τ: int) -> bool:
        if not ((ξ < (λ - 2)) is False):
            return True
        else:
            if not (λ <= 2):
                ς = λ - 3

                def ζ(μ: int) -> bool:
                    if μ > ς:
                        return True
                    else:
                        # Check that string_input[μ], string_input[μ+1], string_input[μ+2] are all equal
                        if not (
                            (not (string_input[μ] != string_input[μ + 1]))
                            and (not (string_input[μ + 1] != string_input[μ + 2]))
                            and (not (string_input[μ] != string_input[μ + 2]))
                        ):
                            return False
                        else:
                            return ζ(μ + 1)

                return ζ(0)
            else:
                return False

    return ʎɹɐƃɹnƎ(len(string_input), 0, 0)