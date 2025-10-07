from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def ㄧΩΧεΨ(ϗϪ: List[int], ϟɊ: int) -> bool:
        if not (not sum(ϗϪ) <= ϟɊ):
            return False

        def 풕₌₌(Ϡ: List[int], ϫ: int, ϭ: int) -> bool:
            if ϫ <= ϭ:
                if Ϡ[ϫ] != Ϡ[ϭ]:
                    return False
                else:
                    return 풕₌₌(Ϡ, ϫ + 1, ϭ - 1)
            else:
                return True

        return 풕₌₌(list_q, 0, len(list_q) - 1)

    return ㄧΩΧεΨ(list_q, maximum_weight_w)