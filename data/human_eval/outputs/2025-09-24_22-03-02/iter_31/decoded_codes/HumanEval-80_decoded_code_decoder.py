def is_happy(s: str) -> bool:
    length_s = len(s)
    if length_s < 3:
        return False
    limit = length_s - 2
    for i in range(limit):
        first_char = s[i]
        second_char = s[i + 1]
        third_char = s[i + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
    return True