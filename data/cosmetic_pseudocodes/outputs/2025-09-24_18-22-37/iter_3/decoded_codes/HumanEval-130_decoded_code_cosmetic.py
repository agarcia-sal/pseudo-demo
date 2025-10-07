from typing import List


def tri(integer_n: int) -> List[float]:
    def build_tri(current_index: int, limit: int, acc_list: List[float]) -> List[float]:
        if current_index > limit:
            return acc_list
        if (current_index % 2) == 0:
            value: float = (current_index / 2) + 1
        else:
            prev1 = acc_list[current_index - 1]
            prev2 = acc_list[current_index - 2]
            value = prev1 + prev2 + ((current_index + 3) / 2)
        acc_list.append(value)
        return build_tri(current_index + 1, limit, acc_list)

    if integer_n == 0:
        return [1]
    else:
        initial_array: List[float] = [1, 3]
        return build_tri(2, integer_n, initial_array)