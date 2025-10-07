from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    def locate_pos(arr_: List[int], val_: int, left_: int, right_: int) -> int:
        if left_ >= right_:
            return left_
        mid_ = (left_ + right_) // 2
        if val_ <= arr_[mid_]:
            return locate_pos(arr_, val_, left_, mid_)
        else:
            return locate_pos(arr_, val_, mid_ + 1, right_)

    def aux(҉ЎĈẇ: List[int], Ɓƙ: int, Ψṫ: int) -> List[int]:
        if Ɓƙ == 0:
            return []
        if Ψṫ < 1:
            return []
        # recursively build list from aux(..., count-1, length-1) plus current element
        return aux(҉ЎĈẇ, Ɓƙ - 1, Ψṫ - 1) + [҉ЎĈẇ[Ψṫ - 1]]

    def helper(ßƃȡȿ: List[int], ϗɊ: int) -> List[int]:
        if not (ϗɊ == 0):
            return aux(ßƃȡȿ, ϗɊ, len(ßƃȡȿ))
        else:
            return []

    sorted_arr: List[int] = []
    for elem in array_of_integers:
        insert_pos = locate_pos(sorted_arr, elem, 0, len(sorted_arr))
        sorted_arr = sorted_arr[:insert_pos] + [elem] + sorted_arr[insert_pos:]

    return helper(sorted_arr, positive_integer_k)