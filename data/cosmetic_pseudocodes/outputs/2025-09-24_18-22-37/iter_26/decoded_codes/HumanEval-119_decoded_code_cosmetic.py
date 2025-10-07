from typing import Callable

def match_parens(a_pair: str) -> str:
    def check(candidate: str) -> bool:
        count_tracker: int = 0
        idx: int = 0
        length: int = len(candidate)
        while idx < length:
            current_char: str = candidate[idx]
            idx += 1
            if current_char == '(':
                count_tracker += 1
            else:
                count_tracker -= 1
            if count_tracker < 0:
                return False
        return count_tracker == 0

    first_concat: str = a_pair[0] + a_pair[1]
    second_concat: str = a_pair[1] + a_pair[0]
    if check(second_concat) or check(first_concat):
        return 'Yes'
    return 'No'