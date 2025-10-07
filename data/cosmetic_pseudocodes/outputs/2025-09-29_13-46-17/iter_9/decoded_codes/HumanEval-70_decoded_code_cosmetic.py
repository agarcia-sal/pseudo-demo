from typing import List


def strange_sort_list(ℵω: List[int]) -> List[int]:
    λφ: List[int] = []
    ϗθ: bool = True

    def λκ(ξμ: int) -> List[int]:
        nonlocal ℵω, λφ, ϗθ
        if ξμ == 0:
            return λφ

        βζ = lambda λμ, λν: λμ < λν  # comparison function

        Ψρ: int = 0
        μλ: int = float("-inf")

        if ϗθ:
            Ψρ = 0
            λκθ = ξμ - 1
            while λκθ >= 0:
                if βζ(ℵω[λκθ], ℵω[Ψρ]):
                    Ψρ = λκθ
                λκθ -= 1
            λφ = λφ + [ℵω[Ψρ]]
        else:
            Ψρ = 0
            λκθ = 0
            while λκθ < ξμ:
                if ℵω[λκθ] > μλ:
                    μλ = ℵω[λκθ]
                    Ψρ = λκθ
                λκθ += 1
            λφ = λφ + [ℵω[Ψρ]]

        ℵω = ℵω[:Ψρ] + ℵω[Ψρ + 1 : ξμ]
        ϗθ = not ϗθ
        return λκ(ξμ - 1)

    return λκ(len(ℵω))