from typing import List

def tri(integer_n: int) -> List[int]:
    def loop_rec(current_idx: int, accum_list: List[int]) -> List[int]:
        if current_idx > integer_n:
            return accum_list
        rem = current_idx % 2
        if rem == 0:
            new_val = (current_idx // 2) + 1
        else:
            # current_idx -1 and current_idx -2 are valid indices since current_idx >= 2
            new_val = accum_list[current_idx - 1] + accum_list[current_idx - 2] + ((current_idx + 3) // 2)
        return loop_rec(current_idx + 1, accum_list + [new_val])

    if integer_n == 0:
        return [1]
    return loop_rec(2, [1, 3])