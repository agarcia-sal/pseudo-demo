def count_upper(str_param: str) -> int:
    tally: int = 0
    idx: int = 0
    vowels = {"A", "E", "I", "O", "U"}
    while idx < len(str_param):
        if str_param[idx] in vowels:
            tally += 1
        idx += 2
    return tally