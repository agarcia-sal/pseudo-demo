from typing import List


def tri(integer_n: int) -> List[int]:
    def accumulate_recursive(curr_idx: int, collected: List[int]) -> List[int]:
        if curr_idx > integer_n:
            return collected
        else:
            if curr_idx % 2 != 0:
                val_to_add = collected[curr_idx - 1] + collected[curr_idx - 2] + ((curr_idx + 3) // 2)
            else:
                val_to_add = (curr_idx // 2) + 1
            updated_list = collected + [val_to_add]
            return accumulate_recursive(curr_idx + 1, updated_list)

    if integer_n == 0:
        return [1]
    else:
        initial_seq = [1, 3]
        return accumulate_recursive(2, initial_seq)