def solve(integer_N: int) -> str:
    accumulator: int = 0
    string_form: str = str(integer_N)
    index_counter: int = 0
    while index_counter < len(string_form):
        current_symbol: str = string_form[index_counter]
        numeric_value: int = int(current_symbol)
        accumulator += numeric_value
        index_counter += 1
    full_binary_str: str = bin(accumulator)
    result_str: str = full_binary_str[2:]
    return result_str