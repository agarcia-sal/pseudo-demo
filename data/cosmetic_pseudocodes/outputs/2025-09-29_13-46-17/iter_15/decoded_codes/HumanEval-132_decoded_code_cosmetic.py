from typing import List


def is_nested(string: str) -> bool:
    def φΞΩ(λψχΩ: List[str], μθɸ: List[str]) -> int:
        if not μθɸ or not λψχΩ:
            return 0
        if λψχΩ[-1] == '[':
            return φΞΩ(λψχΩ[:-1], μθɸ) + 1
        else:
            return φΞΩ(λψχΩ, μθɸ[1:])

    ΛΣΩΨ: List[int] = []
    ℜϴΠ: List[int] = []
    Фωψσ: int = 0  # unused variable

    def 𝜴ψς(ζψ: int, ϐλ: int) -> None:
        # ϐλ parameter is unused but preserved per spec
        if ζψ == len(string):
            return
        if string[ζψ] == '[':
            ΛΣΩΨ.append(ζψ)
        else:
            ℜϴΠ.append(ζψ)
        𝜴ψς(ζψ + 1, ϐλ)

    𝜴ψς(0, 0)

    def reverse_list(Ξϗ: List[int]) -> List[int]:
        if len(Ξϗ) < 2:
            return Ξϗ
        ΥΦ = Ξϗ[0]
        Дη = Ξϗ[1:]

        def recursive_reverse(Дη_inner: List[int]) -> List[int]:
            if not Дη_inner:
                return [ΥΦ]
            ΠΞ = Дη_inner[0]
            ΣД = Дη_inner[1:]
            ΨΛ = recursive_reverse(ΣД)
            return ΨΛ + [ΠΞ]

        return recursive_reverse(Дη)

    ℜϴΠ = reverse_list(ℜϴΠ)

    ΦζξΨ = 0
    кос = 0
    ζθ = len(ℜϴΠ)

    def λδξ(κξψ: int) -> None:
        nonlocal ΦζξΨ, кос
        if κξψ == len(ΛΣΩΨ):
            return
        if кос < ζθ and ΛΣΩΨ[κξψ] < ℜϴΠ[кос]:
            ΦζξΨ += 1
            кос += 1
        λδξ(κξψ + 1)

    λδξ(0)

    return not (ΦζξΨ < 2)