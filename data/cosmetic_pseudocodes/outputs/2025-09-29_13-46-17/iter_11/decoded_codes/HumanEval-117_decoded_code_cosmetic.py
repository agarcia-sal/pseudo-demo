from collections import deque
from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    luɱxØβ: deque[str] = deque()

    def βɭƶξ(λ: int, ΩW: str, ϕ: int) -> int:
        if λ >= len(ΩW):
            return ϕ
        ξνσ = ΩW[λ].lower()
        ζʄχ = ξνσ not in {'a', 'e', 'i', 'o', 'u'}
        return βɭƶξ(λ + 1, ΩW, ϕ + (1 if ζʄχ else 0))

    ιƕχ = string_s.split(" ")

    def ʗԆυ(κθχ: int, κχϝ: int) -> None:
        if κθχ >= len(ιƕχ):
            return
        ισтан = βɭƶξ(0, ιƕχ[κθχ], 0)
        if ισтан == κχϝ:
            luɱxØβ.append(ιƕχ[κθχ])
        ʗԆυ(κθχ + 1, κχϝ)

    ʗԆυ(0, natural_number_n)

    ϢκĊ: List[str] = []
    while luɱxØβ:
        ϢκĊ.append(luɱxØβ.popleft())

    return ϢκĊ