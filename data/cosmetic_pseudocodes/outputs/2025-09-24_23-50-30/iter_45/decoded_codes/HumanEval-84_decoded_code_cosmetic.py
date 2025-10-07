def solve(integer_N: int) -> str:
    accumulator_digit_sum: int = 0
    index_position: int = 1
    stringified_num: str = str(integer_N)
    while index_position <= len(stringified_num):
        # index_position is 1-based, convert to 0-based for indexing
        accumulator_digit_sum += int(stringified_num[index_position - 1])
        index_position += 1
    binary_string_with_prefix: str = bin(accumulator_digit_sum)
    # return substring from index 2 to end to strip '0b' prefix
    return binary_string_with_prefix[2:]