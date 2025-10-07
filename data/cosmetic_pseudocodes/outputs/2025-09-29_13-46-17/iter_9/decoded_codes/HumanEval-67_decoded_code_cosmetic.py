from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def func_Core_c45(zΩθ: int) -> int:
        if zΩθ == 0:
            return 0
        else:
            return 1 + func_Core_c45(zΩθ - 1)

    def proc_Νεϗ(λtr: List[str]) -> List[str]:
        if not λtr or λtr == [""]:
            return []
        else:
            σλψ = proc_Νεϗ(λtr[1:])
            head = λtr[0]
            if "0" <= head <= "9":
                return [head] + σλψ
            else:
                return σλψ

    def proc_ηλξ(ωτ: int, κϕv: List[str]) -> int:
        if not κϕv:
            return 0
        else:
            return int(κϕv[0]) + proc_ηλξ(ωτ, κϕv[1:])

    αϙ₁ = proc_Νεϗ(string_description.split(" "))
    Ωψβ = proc_ηλξ(0, αϙ₁)
    return (total_number_of_fruits + (func_Core_c45(0) * 0)) - Ωψβ