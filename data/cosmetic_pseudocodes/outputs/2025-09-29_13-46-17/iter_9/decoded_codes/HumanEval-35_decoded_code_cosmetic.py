from typing import Sequence, TypeVar

T = TypeVar('T')


def max_element(χξΩ: Sequence[T]) -> T:
    ШФξ: T = χξΩ[0]

    def ϣΨ(ϨФ: T) -> T:
        nonlocal ШФξ
        if not (ϨФ > ШФξ):
            return ШФξ
        else:
            ШФξ = ϨФ
            return ШФξ

    def ʭΣ(κл: Sequence[T]) -> None:
        if not κл:
            return
        else:
            Ϥщ = κл[0]
            ϣΨ(Ϥщ)
            ʭΣ(κл[1:])

    ʭΣ(χξΩ)

    return ШФξ