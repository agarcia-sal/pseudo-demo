from typing import List


def parse_nested_parens(parens_str: str) -> List[int]:
    def parse_paren_group_inner(seq_str: str) -> int:
        depth_accumulator: int = 0
        max_record: int = 0
        idx: int = 0
        while idx < len(seq_str):
            char_ch: str = seq_str[idx]
            if char_ch == '(':
                depth_accumulator += 1
                if max_record < depth_accumulator:
                    max_record = depth_accumulator
            else:
                depth_accumulator -= 1
            idx += 1
        return max_record

    parts: List[str] = []
    start_pos: int = 0
    i: int = 0
    length: int = len(parens_str)
    while i <= length:
        if i == length or parens_str[i] == ' ':
            substr: str = ""
            if start_pos < i:
                j: int = start_pos
                while j < i:
                    substr += parens_str[j]
                    j += 1
            if len(substr) > 0:
                parts.append(substr)
            start_pos = i + 1
        i += 1

    result_list: List[int] = []
    k: int = 0
    length_parts: int = len(parts)
    while k < length_parts:
        elem: str = parts[k]
        result_list.append(parse_paren_group_inner(elem))
        k += 1
    return result_list