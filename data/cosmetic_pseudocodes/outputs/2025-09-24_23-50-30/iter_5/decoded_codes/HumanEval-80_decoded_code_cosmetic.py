def is_happy(string_input: str) -> bool:
    position: int = 0
    while position <= len(string_input) - 3:
        a: str = string_input[position]
        b: str = string_input[position + 1]
        c: str = string_input[position + 2]
        if not (a != b and b != c and a != c):
            return False
        position += 1
    return len(string_input) >= 3