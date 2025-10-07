from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        ci_depth = 0
        mx_depth = 0
        length_gs = len(group_string)
        ix = 0

        while ix < length_gs:
            sym = group_string[ix]
            if sym == '(':
                ci_depth += 1
                if ci_depth > mx_depth:
                    mx_depth = ci_depth
            else:
                ci_depth -= 1
            ix += 1

        return mx_depth

    split_groups: List[str] = []
    ps_length = len(parentheses_string)
    index_ptr = 0
    temp_start = 0

    while index_ptr <= ps_length:
        if index_ptr == ps_length or parentheses_string[index_ptr] == ' ':
            candidate_group = parentheses_string[temp_start:index_ptr]
            if candidate_group:
                split_groups.append(candidate_group)
            temp_start = index_ptr + 1
        index_ptr += 1

    results: List[int] = [parse_paren_group(element) for element in split_groups]
    return results