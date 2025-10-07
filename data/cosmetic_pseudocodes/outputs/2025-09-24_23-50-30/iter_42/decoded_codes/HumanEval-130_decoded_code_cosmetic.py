from typing import List


def tri(number_z: int) -> List[int]:
    result_w: List[int] = [1]
    if number_z == 0:
        return result_w
    result_w = [1, 3]

    def helper_loop(pos_v: int, acc_u: List[int]) -> List[int]:
        if pos_v > number_z:
            return acc_u
        if pos_v % 2 == 0:
            acc_u.append((pos_v // 2) + 1)
        else:
            acc_u.append(acc_u[pos_v - 1] + acc_u[pos_v - 2] + ((pos_v + 3) // 2))
        return helper_loop(pos_v + 1, acc_u)

    return helper_loop(2, result_w)