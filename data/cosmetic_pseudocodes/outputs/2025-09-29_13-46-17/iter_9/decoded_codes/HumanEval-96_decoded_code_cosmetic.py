from typing import List


def count_up_to(n: int) -> List[int]:
    def _ζ(n: int, _µ: List[int]) -> List[int]:
        if n < 2:
            return _µ

        def _ψ(j: int) -> bool:
            if j < 2 or j >= n:
                return True
            if n % j == 0:
                return False
            return _ψ(j + 1)

        _χ = _ψ(2)
        _ϵ = _µ + [n] if _χ else _µ
        return _ζ(n - 1, _ϵ)

    return list(reversed(_ζ(n - 1, [])))