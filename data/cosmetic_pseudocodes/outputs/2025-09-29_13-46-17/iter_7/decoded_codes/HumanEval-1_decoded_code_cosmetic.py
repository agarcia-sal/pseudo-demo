from typing import List

def separate_paren_groups(str_input: str) -> List[List[str]]:
    def aux(
        itr_chars: List[str],
        acc_results: List[List[str]],
        acc_current: List[str],
        depth_tracker: int,
    ) -> List[List[str]]:
        # If not inside any parentheses and the current accumulator has content,
        # treat it as a complete group
        if depth_tracker == 0 and acc_current:
            updated_acc_results = acc_results + [acc_current]
        else:
            updated_acc_results = acc_results

        if not itr_chars:
            return updated_acc_results

        h, *t = itr_chars
        if h == '(':
            return aux(t, updated_acc_results, acc_current + [h], depth_tracker + 1)
        elif h == ')':
            new_depth = depth_tracker - 1
            return aux(t, updated_acc_results, acc_current + [h], new_depth)
        else:
            return aux(t, updated_acc_results, acc_current + [h], depth_tracker)

    return aux(list(str_input), [], [], 0)