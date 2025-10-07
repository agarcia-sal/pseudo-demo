def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result_string = []
    for char_candidate in input_string:
        if char_candidate.lower() in vowels:
            continue
        result_string.append(char_candidate)
    return ''.join(result_string)