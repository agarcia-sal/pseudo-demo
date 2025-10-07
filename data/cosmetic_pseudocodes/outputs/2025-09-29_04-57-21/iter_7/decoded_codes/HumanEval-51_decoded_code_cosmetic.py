def remove_vowels(text: str) -> str:
    result_string = []
    index = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index < len(text):
        current_char = text[index]
        lowered_char = current_char.lower()
        if lowered_char not in vowels:
            result_string.append(current_char)
        index += 1
    return ''.join(result_string)