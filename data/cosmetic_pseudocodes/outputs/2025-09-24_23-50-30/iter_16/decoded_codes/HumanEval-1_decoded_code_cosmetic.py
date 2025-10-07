from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def accumulate_groups(
        idx: int,
        depth: int,
        temp_accum: str,
        accum_result: List[str],
    ) -> List[str]:
        if idx >= len(string_of_parentheses):
            return accum_result

        ch = string_of_parentheses[idx]

        if ch == '(':
            return accumulate_groups(idx + 1, depth + 1, temp_accum + ch, accum_result)
        elif ch == ')':
            new_depth = depth - 1
            updated_accum = temp_accum + ch
            if new_depth == 0:
                return accumulate_groups(idx + 1, new_depth, "", accum_result + [updated_accum])
            else:
                return accumulate_groups(idx + 1, new_depth, updated_accum, accum_result)
        else:
            return accumulate_groups(idx + 1, depth, temp_accum, accum_result)

    return accumulate_groups(0, 0, "", [])