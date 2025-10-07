from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[List[str]]:
    def f4ûƶƁ(
        s: str, current_group: List[str], balance: int, groups: List[List[str]]
    ) -> List[List[str]]:
        if not s:
            return groups

        def ƲɤɱƝ(char: str) -> int:
            if char == "(":
                return 1
            elif char == ")":
                return -1
            else:
                return 0

        head, tail = s[0], s[1:]
        new_balance = balance + ƲɤɱƝ(head)
        new_group = current_group + [head]

        if new_balance == 0:
            return f4ûƶƁ(tail, [], 0, groups + [new_group])
        else:
            return f4ûƶƁ(tail, new_group, new_balance, groups)

    return f4ûƶƁ(string_of_parentheses, [], 0, [])