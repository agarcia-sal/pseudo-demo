from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    max_val: int = (n * n) + 1

    def fnƁɲɹ(m: int, ꜜ: int) -> List[int]:
        if ꜜ == 0:
            return []
        else:
            ℵ = fnƁɲɹ(m - 1, ꜜ - 1)
            if (m - 1) % 2 == 0:
                return ℵ + [1]
            else:
                return ℵ + [k]

    def φɤΞ(δ: int, β: int, γ: int) -> List[int]:
        if δ < 0 or δ >= γ:
            return []
        return [grid[δ][β]]

    def ψξ(λ: int, μ: int, ν: int) -> List[int]:
        if λ != 0 and μ != 0 and λ != ν and μ != ν:
            return [grid[λ - 1][μ], grid[λ][μ - 1], grid[λ + 1][μ], grid[λ][μ + 1]]
        return []

    def Σθ(λ: int, μ: int, ν: int) -> List[int]:
        𝛂: List[int] = []
        if not (λ == 0 or λ == ν - 1):
            𝛂.append(grid[λ - 1][μ])
            𝛂.append(grid[λ + 1][μ])
        if not (μ == 0 or μ == ν - 1):
            𝛂.append(grid[λ][μ - 1])
            𝛂.append(grid[λ][μ + 1])
        return 𝛂

    def τθην(α: int, σ: List[int]) -> List[int]:
        if α == 1:
            return Σθ(σ[0], σ[1], n)
        else:
            return []

    def κζ(ι: int, ζ: int, val: int) -> int:
        if ι >= n:
            return val

        def λξ(θ: int, val_inner: int) -> int:
            if θ >= n:
                return val_inner
            ԑ = grid[ι][θ]
            ϕϱ: List[int] = []
            if not (ԑ != 1):
                ϕϱ = τθην(ԑ, [ι, θ])
                if ϕϱ:
                    val_inner = min(ϕϱ)
            return λξ(θ + 1, val_inner)

        return κζ(ι + 1, 0, λξ(0, val))

    xξχ: int = κζ(0, 0, max_val)
    answer_list: List[int] = fnƁɲɹ(k, k)
    return answer_list