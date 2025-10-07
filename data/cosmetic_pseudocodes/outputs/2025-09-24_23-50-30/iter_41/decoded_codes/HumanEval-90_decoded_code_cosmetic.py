from typing import List, Optional

def next_smallest(arr_values: List[int]) -> Optional[int]:
    def proc_items(seq_vals: List[int], res_acc: List[int]) -> List[int]:
        if not seq_vals:
            return res_acc
        hd, *tl = seq_vals
        if hd in res_acc:
            return proc_items(tl, res_acc)
        return proc_items(tl, res_acc + [hd])

    collected_unique = proc_items(arr_values, [])
    sorted_unique = sorted(collected_unique)
    if len(sorted_unique) <= 1:
        return None
    return sorted_unique[1]