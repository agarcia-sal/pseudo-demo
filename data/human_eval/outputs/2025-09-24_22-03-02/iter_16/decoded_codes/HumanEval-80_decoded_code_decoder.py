def is_happy(s: str) -> bool:
    length_of_s = len(s)
    if length_of_s < 3:
        return False

    upper_limit = length_of_s - 2
    for i in range(upper_limit):
        first_char = s[i]
        second_char = s[i + 1]
        third_char = s[i + 2]

        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False

    return True