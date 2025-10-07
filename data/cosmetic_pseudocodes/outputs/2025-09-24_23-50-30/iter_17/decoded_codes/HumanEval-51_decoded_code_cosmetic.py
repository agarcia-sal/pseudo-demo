def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result_chars = []
    index: int = 0
    while index < len(input_string):
        current_char = input_string[index]
        if current_char.lower() not in vowels:
            result_chars.append(current_char)
        index += 1
    return ''.join(result_chars)