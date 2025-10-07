def digitSum(input_str: str) -> int:
    total_value: int = 0
    idx: int = 0
    while idx < len(input_str):
        curr_char: str = input_str[idx]
        if not ('A' <= curr_char <= 'Z'):
            temp_val: int = 0
        else:
            temp_val = ord(curr_char)
        total_value += temp_val
        idx += 1
    return total_value