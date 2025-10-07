from typing import List


def tri(n_val: int) -> List[int]:
    s_result: List[int] = []
    if n_val != 0:
        s_result = [1, 3]
        i_index = 2
        while i_index <= n_val:
            if i_index % 2 == 0:
                s_result.append((i_index // 2) + 1)
            else:
                s_result.append(s_result[i_index - 1] + s_result[i_index - 2] + ((i_index + 3) // 2))
            i_index += 1
    else:
        s_result = [1]
    return s_result