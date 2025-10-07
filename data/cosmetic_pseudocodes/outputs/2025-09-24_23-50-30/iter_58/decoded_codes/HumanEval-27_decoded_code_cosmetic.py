from typing import List

def flip_case(str_1: str) -> str:
    result_9: List[str] = []
    idx_3: int = 0
    while idx_3 < len(str_1):
        ch_5: str = str_1[idx_3]
        if 'a' <= ch_5 <= 'z':
            result_9.append(ch_5.upper())
        elif 'A' <= ch_5 <= 'Z':
            result_9.append(ch_5.lower())
        else:
            result_9.append(ch_5)
        idx_3 += 1
    return ''.join(result_9)