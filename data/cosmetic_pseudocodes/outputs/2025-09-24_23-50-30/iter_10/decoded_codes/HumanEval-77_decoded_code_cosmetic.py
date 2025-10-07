from math import floor

def iscube(input_num: int) -> bool:
    nonnegative_num: int = -input_num if input_num < 0 else input_num
    root_candidate: float = nonnegative_num ** (1/3) + 0.5
    integer_root: int = floor(root_candidate)
    cubic_result: int = integer_root * integer_root * integer_root
    return cubic_result == nonnegative_num