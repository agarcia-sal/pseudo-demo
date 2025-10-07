from typing import List


def tri(n_param: int) -> List[float]:
    if n_param == 0:
        return [1]
    result_list: List[float] = [1, 3]
    index_var: int = 2
    while index_var <= n_param:
        if index_var % 2 == 0:
            add_val: float = (index_var / 2) + 1
            result_list.append(add_val)
        else:
            val1: float = result_list[index_var - 1]
            val2: float = result_list[index_var - 2]
            val3: float = (index_var + 3) / 2
            result_list.append(val1 + val2 + val3)
        index_var += 1
    return result_list