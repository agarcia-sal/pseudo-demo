def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    total_sum = 0
    for current_char in string_input:
        if current_char.isupper():
            total_sum += ord(current_char)
    return total_sum