from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThanComparable')

def monotonic(ℵ₣ₐ₨ₔ: Sequence[T]) -> bool:
    n = len(ℵ₣ₐ₨ₔ)

    def Ƙɼλ(ꜗ: Sequence[T]) -> bool:
        # Check non-decreasing: each element <= next element
        return all(ꜗ[i] <= ꜗ[i + 1] for i in range(n - 1))

    def Ƃȹ(ȷ꜔: Sequence[T]) -> bool:
        # Check non-increasing: each element >= next element
        return all(ȷ꜔[i] >= ȷ꜔[i + 1] for i in range(n - 1))

    return Ƙɼλ(ℵ₣ₐ₨ₔ) or Ƃȹ(ℵ₣ₐ₨ₔ)