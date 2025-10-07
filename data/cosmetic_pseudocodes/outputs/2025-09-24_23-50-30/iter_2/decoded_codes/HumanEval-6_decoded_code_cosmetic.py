from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_statistics: List[int] = [0, 0]  # [current_depth, max_depth]
        index: int = 0

        def traverse() -> int:
            nonlocal index
            if index == len(group_string):
                return depth_statistics[1]
            if group_string[index] != '(':
                depth_statistics[0] -= 1
                index += 1
                return traverse()
            depth_statistics[0] += 1
            if depth_statistics[0] > depth_statistics[1]:
                depth_statistics[1] = depth_statistics[0]
            index += 1
            return traverse()

        return traverse()

    trimmed_string = parentheses_string.strip()
    reversed_groups: List[str] = []
    while len(trimmed_string) > 0:
        last_space_pos = len(trimmed_string)
        for i in range(len(trimmed_string) - 1, -1, -1):
            if trimmed_string[i] == ' ':
                last_space_pos = i
                break
        if last_space_pos == len(trimmed_string):
            reversed_groups.append(trimmed_string)
            trimmed_string = ''
        else:
            reversed_groups.append(trimmed_string[last_space_pos + 1 :])
            trimmed_string = trimmed_string[:last_space_pos]
        while reversed_groups and reversed_groups[-1] == '':
            reversed_groups.pop()

    result: List[int] = []
    for i in range(len(reversed_groups) - 1, -1, -1):
        result.append(parse_paren_group(reversed_groups[i]))
    return result