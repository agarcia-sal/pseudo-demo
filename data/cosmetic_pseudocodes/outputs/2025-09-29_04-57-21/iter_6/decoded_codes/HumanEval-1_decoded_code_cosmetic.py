from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_groups: List[str] = []
    temporary_storage: List[str] = []
    depth_tracker: int = 0

    for symbol in string_of_parentheses:
        if symbol == '(':
            depth_tracker += 1
            temporary_storage.append(symbol)
        elif symbol == ')':
            depth_tracker -= 1
            temporary_storage.append(symbol)

            if depth_tracker == 0:
                group_string = "".join(temporary_storage)
                collected_groups.append(group_string)
                temporary_storage = []

    return collected_groups