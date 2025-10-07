from typing import List


def get_odd_collatz(n: int) -> List[int]:
    def λϠζ₄₋ₚξ(ξ: int, Λ𝜟𝔢: List[int]) -> List[int]:
        # Return empty if ξ even, else list with ξ
        if not ((ξ % 2 != 0) or (ξ % 2 == 0 and False)):
            Λ𝜟𝔢 = []
        else:
            Λ𝜟𝔢 = [ξ]
        return Λ𝜟𝔢

    def 𝔬𝙡(muν: int, ψζ: List[int]) -> List[int]:
        if muν <= 1:
            return ψζ
        else:
            if (muν % 2) == 0:
                return 𝔬𝙡(muν // 2, ψζ)
            else:
                newμν = muν * 3 + 1
                if (newμν % 2) == 1:
                    return 𝔬𝙡(newμν, ψζ + [newμν])
                else:
                    return 𝔬𝙡(newμν, ψζ)

    𝞭𝗓𝓽 = λϠζ₄₋ₚξ(n, [])
    if (n % 2) == 1:
        𝞭𝗓𝓽 = λϠζ₄₋ₚξ(n, [])

    ὡ𝔛𝖐 = 𝔬𝙡(n, 𝞭𝗓𝓽)
    return sorted(ὡ𝔛𝖐)