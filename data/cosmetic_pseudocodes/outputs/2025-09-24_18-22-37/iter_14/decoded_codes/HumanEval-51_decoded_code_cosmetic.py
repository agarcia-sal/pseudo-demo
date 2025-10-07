def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result_builder = []
    iterator_index = 0
    while iterator_index < len(input_string):
        current_char = input_string[iterator_index]
        lowered_char = current_char.lower()
        if lowered_char in vowels:
            pass  # skip vowels
        else:
            result_builder.append(current_char)
        iterator_index += 1
    return ''.join(result_builder)