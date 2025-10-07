from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        cnt = 0
        max_cnt = 0
        for ch in group_string:
            if ch == '(':
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt -= 1
        return max_cnt

    splits: List[str] = []
    start_idx = 0
    length = len(parentheses_string)
    for pos in range(length):
        if parentheses_string[pos] == ' ':
            fragment = parentheses_string[start_idx:pos]
            splits.append(fragment)
            start_idx = pos + 1
    if start_idx <= length - 1:
        splits.append(parentheses_string[start_idx:length])

    filtered_groups = [en for en in splits if en != '']

    results = [parse_paren_group(elem) for elem in filtered_groups]

    return results