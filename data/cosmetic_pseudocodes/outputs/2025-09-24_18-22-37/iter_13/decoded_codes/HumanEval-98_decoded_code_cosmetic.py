def count_upper(parameter_str: str) -> int:
    total: int = 0
    position: int = 0
    vowels: str = "AEIOU"
    while position <= len(parameter_str) - 1:
        current_char: str = parameter_str[position]
        if current_char in vowels:
            total += 1
        position += 2
    return total