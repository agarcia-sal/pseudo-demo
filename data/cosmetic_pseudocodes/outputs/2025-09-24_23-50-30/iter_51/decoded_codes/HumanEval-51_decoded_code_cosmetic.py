def remove_vowels(str_input: str) -> str:
    output_accumulator: str = ""
    position_counter: int = 1
    while position_counter <= len(str_input):
        current_element: str = str_input[position_counter - 1]
        if current_element.lower() not in {"a", "e", "i", "o", "u"}:
            output_accumulator += current_element
        position_counter += 1
    return output_accumulator