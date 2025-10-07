from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_third(seq_param: Sequence[T]) -> List[T]:
    seq_param = list(seq_param)  # make a copy as a list
    subset_vars = [seq_param[idx_var] for idx_var in range(0, len(seq_param), 3)]
    rearranged_vars = sorted(subset_vars)
    counter_var = 0
    for idx_var in range(len(seq_param)):
        if idx_var % 3 == 0:
            seq_param[idx_var] = rearranged_vars[counter_var]
            counter_var += 1
    return seq_param