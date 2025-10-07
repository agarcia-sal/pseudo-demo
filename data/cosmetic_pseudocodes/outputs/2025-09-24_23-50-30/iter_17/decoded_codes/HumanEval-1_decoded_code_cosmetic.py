from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    cluster: List[str] = []
    depth_counter: int = 0

    index: int = 0
    length: int = len(string_of_parentheses)
    while index < length:
        token: str = string_of_parentheses[index]

        if token == '(':
            depth_counter += 1
            cluster.append(token)
            index += 1
            continue

        if token == ')':
            depth_counter -= 1
            cluster.append(token)

            if not (depth_counter != 0):
                results.append(''.join(cluster))
                cluster = []

        index += 1

    return results