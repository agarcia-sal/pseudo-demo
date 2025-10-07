def solve(integer_N: int) -> str:
    accumulation_variable: int = 0
    char_iterable: str = str(integer_N)
    index_counter: int = 0
    while index_counter < len(char_iterable):
        current_element: str = char_iterable[index_counter]
        temp_numeric: int = int(current_element)
        accumulation_variable += temp_numeric
        index_counter += 1
    full_binary_string: str = bin(accumulation_variable)
    trimmed_binary: str = full_binary_string[2:]
    return trimmed_binary