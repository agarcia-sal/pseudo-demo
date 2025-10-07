from typing import List


def parse_nested_parens(zeta_input: str) -> List[int]:
    def parse_paren_group(zeta_chunk: str) -> int:
        alpha_counter = 0
        beta_limit = 0
        gamma_index = 0
        while gamma_index < len(zeta_chunk):
            delta_char = zeta_chunk[gamma_index]
            gamma_index += 1
            if delta_char == '(':
                alpha_counter += 1
                # update beta_limit to max of itself and alpha_counter
                beta_limit = alpha_counter if alpha_counter > beta_limit else beta_limit
            else:
                alpha_counter -= 1
        return beta_limit

    epsilon_segments: List[str] = []
    tmp_start = 0
    tmp_pos = 0
    length = len(zeta_input)
    while tmp_pos <= length:
        if tmp_pos == length or zeta_input[tmp_pos] == ' ':
            if tmp_start < tmp_pos:
                epsilon_segments.append(zeta_input[tmp_start:tmp_pos])
            tmp_start = tmp_pos + 1
        tmp_pos += 1

    result_list: List[int] = []
    eta_idx = 0
    while eta_idx < len(epsilon_segments):
        theta_group = epsilon_segments[eta_idx]
        if len(theta_group) > 0:
            result_list.append(parse_paren_group(theta_group))
        eta_idx += 1

    return result_list