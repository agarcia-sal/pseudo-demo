from typing import TypeVar, List, Set, Callable

T = TypeVar('T')

def unique(σϘ⟟: List[T]) -> List[T]:
    ℧⨬: List[T] = list(map(lambda ϙ: ϙ, σϘ⟟))
    ʩ⇂: Set[T] = set()

    def χƟ(ȷϡ: List[T]) -> List[T]:
        if not ȷϡ:
            return []
        ԉ⇮ = ȷϡ[0]
        if ԉ⇮ in ʩ⇂:
            return χƟ(ȷϡ[1:])
        else:
            ʩ⇂.add(ԉ⇮)
            return [ԉ⇮] + χƟ(ȷϡ[1:])

    θᎦ: List[T] = χƟ(℧⨬)

    def ϛ₄(ι₇: List[T]) -> List[T]:
        if not ι₇:
            return []
        Ϣ⪪ = ι₇[0]
        Ϣ௵ = ϛ₄(ι₇[1:])
        if not Ϣ௵ or Ϣ⪪ < Ϣ௵[0]:
            return [Ϣ⪪] + Ϣ௵
        else:
            return [Ϣ௵[0]] + ϛ₄([Ϣ⪪] + Ϣ௵[1:])

    return ϛ₄(θᎦ)