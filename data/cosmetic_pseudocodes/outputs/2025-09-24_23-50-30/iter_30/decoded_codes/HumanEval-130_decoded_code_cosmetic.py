from typing import List


def tri(param_x: int) -> List[int]:
    if param_x == 0:
        return [1]
    else:
        array_res: List[int] = [1, 3]
        index_var: int = 2
        while index_var <= param_x:
            if not (index_var % 2 == 0):  # index_var is odd
                element = (
                    array_res[index_var - 1]
                    + array_res[index_var - 2]
                    + ((index_var + 3) // 2)
                )
                array_res.append(element)
            else:  # index_var is even
                array_res.append((index_var // 2) + 1)
            index_var += 1
        return array_res