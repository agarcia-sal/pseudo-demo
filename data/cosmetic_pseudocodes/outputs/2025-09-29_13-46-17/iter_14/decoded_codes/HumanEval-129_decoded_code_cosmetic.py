from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    INF: int = n * n + 1

    def 𝒲ꝉ𝇙(σ: int, ѳ: int) -> List[int]:
        if σ < 0 or ѳ < 0 or σ >= n or ѳ >= n:
            return []
        return [grid[σ][ѳ]]

    def 𐑒𐐬𐑷(λ: int, ψ: int) -> int:
        if λ < 0 or ψ < 0 or λ >= n or ψ >= n:
            return INF
        if grid[λ][ψ] != 1:
            return INF
        up = 𐑒𐐬𐑷(λ - 1, ψ)
        left = 𐑒𐐬𐑷(λ, ψ - 1)
        down = 𐑒𐐬𐑷(λ + 1, ψ)
        right = 𐑒𐐬𐑷(λ, ψ + 1)
        return min(up, left, down, right)

    ɧ㉪ᴥ = 𐑒𐐬𐑷(0, 0) + 1

    def 𝒔Ôŋ(ŵ: int, ɱ: int, ø: List[int]) -> List[int]:
        if ɱ == k:
            return ø
        ϗɶ = 1 if ɱ % 2 == 0 else ɧ㉪ᴥ
        return 𝒔Ôŋ(ŵ, ɱ + 1, ø + [ϗɶ])

    return 𝒔Ôŋ(minPath, 0, [])