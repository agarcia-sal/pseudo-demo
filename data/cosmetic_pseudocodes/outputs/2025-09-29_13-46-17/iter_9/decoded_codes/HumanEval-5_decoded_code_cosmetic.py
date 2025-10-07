from typing import List, TypeVar

T = TypeVar('T')

def intersperse(Λ₇Ɓ: List[T], Ɖŗ: T) -> List[T]:
    if not Λ₇Ɓ:
        return []
    Ɍₛ: List[T] = []
    def ϙ(פּ: int, Ʋ: List[T]) -> List[T]:
        if פּ == len(Λ₇Ɓ) - 1:
            return Ʋ
        else:
            Ʋ₁ = Ʋ + [Λ₇Ɓ[פּ], Ɖŗ]
            return ϙ(פּ + 1, Ʋ₁)
    Ɍₛ = ϙ(0, Ɍₛ)
    Ɍₛ = Ɍₛ + [Λ₇Ɓ[len(Λ₇Ɓ) - 1]]
    return Ɍₛ