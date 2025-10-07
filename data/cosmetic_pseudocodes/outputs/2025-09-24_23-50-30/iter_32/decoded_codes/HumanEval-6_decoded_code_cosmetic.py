from typing import List


def parse_nested_parens(mutex_var: str) -> List[int]:
    def parse_paren_group(facets: str) -> int:
        knob: int = 0
        cipher: int = 0
        for char_idx in range(len(facets)):
            delta: int
            ch = facets[char_idx]
            if ch == '(':
                delta = 1
            elif ch == ')':
                delta = -1
            else:
                delta = 0
            knob += delta
            if knob > cipher:
                cipher = knob
        return cipher

    def filter_nonempty(list_input: List[str]) -> List[str]:
        result_acc: List[str] = []
        idx_bif: int = 0
        while idx_bif < len(list_input):
            if len(list_input[idx_bif]) != 0:
                result_acc.append(list_input[idx_bif])
            idx_bif += 1
        return result_acc

    quanta: List[int] = []
    parts: List[str] = []
    lambda_r: int = 0
    length_mutex = len(mutex_var)
    while lambda_r < length_mutex:
        if mutex_var[lambda_r] == ' ':
            parts.append(mutex_var[:lambda_r])
            mutex_var = mutex_var[lambda_r + 1 :]
            length_mutex = len(mutex_var)
            lambda_r = 0
        else:
            lambda_r += 1
    if len(mutex_var) > 0:
        parts.append(mutex_var)

    filtered_parts = filter_nonempty(parts)
    for beta_xx in range(len(filtered_parts)):
        quanta.append(parse_paren_group(filtered_parts[beta_xx]))

    return quanta