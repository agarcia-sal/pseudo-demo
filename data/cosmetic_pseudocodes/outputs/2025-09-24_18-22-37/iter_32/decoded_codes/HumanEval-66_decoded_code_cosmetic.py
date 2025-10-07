def digitSum(input_sequence: str) -> int:
    if input_sequence == "":
        return 0

    total_sum: int = 0
    index_counter: int = 0
    length_limit: int = len(input_sequence)

    while index_counter < length_limit:
        current_char: str = input_sequence[index_counter]
        is_uppercase_flag: bool = 'A' <= current_char <= 'Z'

        if is_uppercase_flag:
            total_sum += ord(current_char)

        index_counter += 1

    return total_sum