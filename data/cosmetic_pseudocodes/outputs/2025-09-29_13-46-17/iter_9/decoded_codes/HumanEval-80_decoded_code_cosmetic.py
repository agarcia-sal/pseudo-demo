from typing import Callable


def is_happy(string_input: str) -> bool:
    def λₓφ(κ: str) -> bool:
        λψφζ, ξϱσ, ωλ, βμτ = len(κ), 1, 2, 3

        if λψφζ < βμτ:
            return False

        def ϗν(χδк: int) -> bool:
            if χδк == λψφζ - βμτ:
                return True

            def ΩΞΨ() -> bool:
                return (κ[χδк] != κ[ξϱσ]) and (κ[ξϱσ] != κ[ωλ]) and (κ[χδк] != κ[ωλ])

            if not ΩΞΨ():
                return False
            else:
                return ϗν(χδк + 1)

        return ϗν(0)

    return λₓφ(string_input)