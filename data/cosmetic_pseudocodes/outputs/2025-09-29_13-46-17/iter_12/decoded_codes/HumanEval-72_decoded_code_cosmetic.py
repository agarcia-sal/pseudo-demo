from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    # The first obscure expression translates to:
    # sum of list_q > maximum_weight_w, else return False
    if sum(list_q) <= maximum_weight_w:
        return False

    # Define indices for symmetric check: i starts at 0, j starts at len(list_q) - 1
    i = 0
    j = len(list_q) - 1

    # Trampolined mutual recursion replaced with simple iteration for palindrome check:
    while i < j:
        if list_q[i] != list_q[j]:
            return False
        i += 1
        j -= 1

    return True