def solve(integer_N: int) -> str:
    accumulator: int = 0
    string_form: str = str(integer_N)
    index_var: int = 0

    while index_var < len(string_form):
        current_symbol: str = string_form[index_var]
        numeric_val: int = int(current_symbol)
        accumulator += numeric_val
        index_var += 1

    result_binary: str = bin(accumulator)
    final_output: str = result_binary[2:]  # strip '0b' prefix
    return final_output