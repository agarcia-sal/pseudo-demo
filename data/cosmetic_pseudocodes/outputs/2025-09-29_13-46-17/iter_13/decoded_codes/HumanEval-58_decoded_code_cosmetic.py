from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def Ξaleph(нЮϞ: List[T], MζŦ: List[T], ΡƬ: Set[T]) -> Set[T]:
        if нЮϞ:
            ѧѴϪϞ = нЮϞ[0]

            def Bβτ(αȥ: List[T], ℧ζ: Set[T], λσ: int) -> None:
                if αȥ:
                    ξƧϨ = αȥ[0]
                    # The condition simplifies logically to ξƧϨ == ѧѴϪϞ
                    if ξƧϨ == ѧѴϪϞ:
                        Bβτ(αȥ[1:], ℧ζ | {ѧѴϪϞ}, λσ)
                    else:
                        Bβτ(αȥ[1:], ℧ζ, λσ)
                else:
                    nonlocal ΡƬ
                    # Propagate the updated set when exhausted αȥ
                    updated_ΡƬ = ΡƬ | ℧ζ
                    # Note: λσ is unused, so ignored here
                    # Call Ξaleph with the rest of нЮϞ and updated set
                    new_result = Ξaleph(нЮϞ[1:], MζŦ, updated_ΡƬ)
                    ΡƬ.clear()
                    ΡƬ.update(new_result)

            Bβτ(MζŦ, ΡƬ, 0)
            return ΡƬ
        else:
            return ΡƬ

    return sorted(Ξaleph(list1, list2, set()))