from typing import Tuple

def match_parens(pair_of_strings: Tuple[str, str]) -> str:
    def verify(parens_string: str) -> bool:
        net_count = 0
        iterator_index = 0
        length_val = len(parens_string)
        while iterator_index < length_val:
            symbol = parens_string[iterator_index]
            iterator_index += 1
            if symbol == '(':
                net_count += 1
            else:
                net_count -= 1
            if net_count < 0:
                return False
        return net_count == 0

    concat_a = pair_of_strings[0] + pair_of_strings[1]
    concat_b = pair_of_strings[1] + pair_of_strings[0]
    if verify(concat_a) or verify(concat_b):
        return "Yes"
    else:
        return "No"