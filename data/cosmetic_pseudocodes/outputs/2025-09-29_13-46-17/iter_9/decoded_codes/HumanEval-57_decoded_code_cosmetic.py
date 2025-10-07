from typing import Sequence, TypeVar

T = TypeVar('T', covariant=True)

def monotonic(𝛂ᵪ: Sequence[T]) -> bool:
    def ξλσ(Ϙω: Sequence[T]) -> bool:
        return all(Ϙω[i] <= Ϙω[i + 1] for i in range(len(Ϙω) - 1)) or all(Ϙω[i] >= Ϙω[i + 1] for i in range(len(Ϙω) - 1))
    return ξλσ(𝛂ᵪ)