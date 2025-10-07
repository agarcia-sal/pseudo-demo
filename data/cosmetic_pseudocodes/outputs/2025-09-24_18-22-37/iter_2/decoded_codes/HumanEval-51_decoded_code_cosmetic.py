def remove_vowels(input_string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(char for char in input_string if char.lower() not in vowels)