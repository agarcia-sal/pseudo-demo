from typing import List, Optional, Set

def common(list1: List[int], list2: List[int]) -> List[int]:
    result_accumulator: Set[int] = set()

    def check_match(a: int, b: int) -> Optional[int]:
        # Return a if a == b else None
        return a if a == b else None

    def recurse_l1(idx_l1: int, accr: Set[int]) -> Set[int]:
        if idx_l1 >= len(list1):
            return accr
        else:
            return recurse_l2(0, accr, list1[idx_l1])

    def recurse_l2(idx_l2: int, accr_l2: Set[int], val: int) -> Set[int]:
        if idx_l2 >= len(list2):
            return recurse_l1(idx_l1=idx_l1 + 1, accr=accr_l2)
        else:
            matched_val = check_match(val, list2[idx_l2])
            new_accr = accr_l2 | {matched_val} if matched_val is not None else accr_l2
            return recurse_l2(idx_l2 + 1, new_accr, val)

    # The above recurse_l2 needs idx_l1, but idx_l1 is from recurse_l1 scope.
    # To fix the closure scope issue, rewrite recur_l1 and recur_l2 as follows:

    def recurse_l1_wrap(idx_l1: int, accr: Set[int]) -> Set[int]:
        if idx_l1 < len(list1):
            return recurse_l2_wrap(0, accr, list1[idx_l1], idx_l1)
        else:
            return accr

    def recurse_l2_wrap(idx_l2: int, accr_l2: Set[int], val: int, idx_l1: int) -> Set[int]:
        if idx_l2 < len(list2):
            new_accr = accr_l2 | {val} if val == list2[idx_l2] else accr_l2
            return recurse_l2_wrap(idx_l2 + 1, new_accr, val, idx_l1)
        else:
            return recurse_l1_wrap(idx_l1 + 1, accr_l2)

    final_set = recurse_l1_wrap(0, result_accumulator)
    return sorted(final_set)