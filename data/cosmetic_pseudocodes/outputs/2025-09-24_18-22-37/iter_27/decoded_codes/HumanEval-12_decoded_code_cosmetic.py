from typing import Optional, Sequence

def longest(tuples: Sequence[str]) -> Optional[str]:
    if not tuples:
        return None

    max_size: int = 0

    for current_str in tuples:
        len_tmp: int = len(current_str)
        if len_tmp > max_size:
            max_size = len_tmp

    for str_target in tuples:
        if len(str_target) == max_size:
            return str_target

    return None  # fallback, though unreachable given input constraints