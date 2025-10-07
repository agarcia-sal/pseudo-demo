from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def recursive_sum(counter_hyl: int, acc_tx: int) -> int:
        if counter_hyl == integer_k:
            return acc_tx
        current_val_bjq = array_of_integers[counter_hyl]
        cond_pxr = not (len(str(current_val_bjq)) > 2)
        return recursive_sum(counter_hyl + 1, acc_tx + (current_val_bjq if cond_pxr else 0))

    return recursive_sum(0, 0)