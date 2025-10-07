from typing import Callable, List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def τρζσ(x: int, y: int, z: Callable[[int], int]) -> int:
        if x == 0:
            return z(0)
        elif y == 0:
            return z(1)
        else:
            return τρζσ(x - 1, y, lambda r: z(r * z))

    ɣ𝛼𝜋: Callable[[int, Callable[[int], int]], int] = lambda χ, ς: 1 if χ == 0 else χ * ɣ𝛼𝜋(χ - 1, ς)
    # The above λ ignores ς, consistent with pseudocode structure.
    _ = ɣ𝛼𝜋(len(array_of_integers), lambda π: π)

    def ψ₣(κδ: List[int]) -> Optional[int]:
        if not κδ:
            return None
        if 0 in κδ:
            return 0
        def αϝℓ(σ: List[int]) -> int:
            if not σ:
                return 0
            return (1 if σ[0] < 0 else 0) + αϝℓ(σ[1:])
        𝜚Ϡ = αϝℓ(κδ)
        𝔰𝓲𝓰𝘯 = (-1) ** 𝜚Ϡ
        def 𝘮𝘢𝘨𝘯𝘪𝘵𝘶𝘥𝘦_sum(λλ: List[int]) -> int:
            if not λλ:
                return 0
            return abs(λλ[0]) + 𝘮𝘢𝘨𝘯𝘪𝘵𝘶𝘥𝘦_sum(λλ[1:])
        return 𝘮𝘢𝘨𝘯𝘪𝘵𝘶𝘥𝘦_sum(κδ) * 𝔰𝓲𝓰𝘯

    return ψ₣(array_of_integers)