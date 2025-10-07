def digitSum(input_string: str) -> int:
    total_value: int = 0
    index_counter: int = len(input_string) - 1
    while index_counter >= 0:
        current_chr: str = input_string[index_counter]
        if not ('A' <= current_chr <= 'Z'):
            index_counter -= 1
            continue
        total_value += ord(current_chr)
        index_counter -= 1
    return total_value