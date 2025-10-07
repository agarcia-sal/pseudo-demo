def remove_vowels(input_string: str) -> str:
    idx: int = 0
    result: str = ""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while idx < len(input_string):
        current_char = input_string[idx]
        if current_char.lower() not in vowels:
            result += current_char
        idx += 1
    return result