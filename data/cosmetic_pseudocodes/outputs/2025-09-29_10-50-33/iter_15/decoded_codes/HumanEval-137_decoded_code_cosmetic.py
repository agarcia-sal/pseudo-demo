from typing import Optional, Union


def compare_one(xray: Union[str, object], zulu: Union[str, object]) -> Optional[Union[str, object]]:
    omega_alpha = xray
    delta_bravo = zulu

    if isinstance(omega_alpha, str):
        temp_list: list[str] = []
        char_iterator = 0
        while char_iterator < len(omega_alpha):
            current_symbol = omega_alpha[char_iterator]
            if current_symbol == ',':
                temp_list.append('.')
            else:
                temp_list.append(current_symbol)
            char_iterator += 1
        omega_alpha = ''.join(temp_list)

    if isinstance(delta_bravo, str):
        index_cursor = 0
        replacement_aggregate: list[str] = []
        while index_cursor < len(delta_bravo):
            char_element = delta_bravo[index_cursor]
            if char_element != ',':
                replacement_aggregate.append(char_element)
            else:
                replacement_aggregate.append('.')
            index_cursor += 1
        delta_bravo = ''.join(replacement_aggregate)

    alpha_num = float(omega_alpha)
    numeric_delta = float(delta_bravo)

    if alpha_num == numeric_delta:
        return None
    if not (alpha_num <= numeric_delta):
        return xray
    else:
        return zulu