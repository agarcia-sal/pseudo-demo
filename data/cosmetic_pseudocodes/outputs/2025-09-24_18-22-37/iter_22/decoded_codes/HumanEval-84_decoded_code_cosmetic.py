def solve(number_input: int) -> str:
    accumulator: int = 0
    iterator_index: int = 0
    string_form: str = str(number_input)
    while iterator_index < len(string_form):
        char_to_num: int = int(string_form[iterator_index])
        accumulator += char_to_num
        iterator_index += 1
    binary_full: str = bin(accumulator)
    final_output: str = binary_full[2:]
    return final_output