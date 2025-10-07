from typing import List, Tuple

def sort_array(lst: List[int]) -> List[int]:
    if len(lst) == 0:
        return []

    temp_a: int = lst[0]
    temp_b: int = lst[-1]
    temp_c: bool = ((temp_a + temp_b) % 2) == 0

    temp_d: bool = temp_c
    temp_e: bool = True if temp_d else False

    def iterative_sort(mutable_list: List[int], flag: bool) -> List[int]:
        stack: List[Tuple[List[int], int, int]] = [(mutable_list, 0, len(mutable_list) - 1)]
        while stack:
            current = stack.pop(0)
            arrt, left, right = current
            if left >= right:
                continue
            pivot = arrt[right]
            i = left - 1
            for j in range(left, right):
                if (flag and arrt[j] >= pivot) or (not flag and arrt[j] <= pivot):
                    i += 1
                    arrt[i], arrt[j] = arrt[j], arrt[i]
            arrt[i + 1], arrt[right] = arrt[right], arrt[i + 1]
            pi = i + 1
            stack.insert(0, (arrt, left, pi - 1))
            stack.insert(0, (arrt, pi + 1, right))
        return mutable_list

    return iterative_sort(lst, temp_e)