from typing import Tuple, Dict


def even_odd_palindrome(p: int) -> Tuple[int, int]:
    mapping: Dict[str, int] = {'ev': 0, 'od': 0}

    def check_pal(num: int) -> bool:
        str_num = str(num)
        rev_str = ''
        idx = len(str_num) - 1
        while idx >= 0:
            rev_str += str_num[idx]
            idx -= 1
        return rev_str == str_num

    curr = 1
    while curr <= p:
        if not check_pal(curr):
            curr += 1
            continue
        if curr % 2 == 0:
            mapping['ev'] += 1
        else:
            mapping['od'] += 1
        curr += 1

    return mapping['ev'], mapping['od']