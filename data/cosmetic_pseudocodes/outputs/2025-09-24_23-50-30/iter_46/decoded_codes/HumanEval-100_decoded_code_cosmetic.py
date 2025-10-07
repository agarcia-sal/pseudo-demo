from typing import List


def make_a_pile(arg1: int) -> List[int]:
    def rec_build(acc_list: List[int], idx: int) -> List[int]:
        if idx < arg1:
            new_val = arg1 + (idx << 1)
            return rec_build(acc_list + [new_val], idx + 1)
        else:
            return acc_list

    return rec_build([], 0)