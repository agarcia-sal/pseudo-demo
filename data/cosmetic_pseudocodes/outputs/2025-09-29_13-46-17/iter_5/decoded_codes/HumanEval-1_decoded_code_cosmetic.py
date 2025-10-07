from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def unwind(idx: int, acc_groups: List[str], acc_chars: List[str], depth: int) -> List[str]:
        if idx == len(string_of_parentheses):
            return acc_groups
        c = string_of_parentheses[idx]
        if c not in ('(', ')'):
            return unwind(idx + 1, acc_groups, acc_chars, depth)
        if c == '(':
            new_depth = depth + 1
            return unwind(idx + 1, acc_groups, acc_chars + [c], new_depth)
        # c == ')'
        new_depth = depth - 1
        new_acc_chars = acc_chars + [c]
        if new_depth == 0:
            group = "".join(new_acc_chars)
            return unwind(idx + 1, acc_groups + [group], [], new_depth)
        return unwind(idx + 1, acc_groups, new_acc_chars, new_depth)

    return unwind(0, [], [], 0)