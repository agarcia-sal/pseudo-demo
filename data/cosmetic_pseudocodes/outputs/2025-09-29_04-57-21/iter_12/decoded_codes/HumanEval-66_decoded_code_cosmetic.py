def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    aggregate_sum = 0
    for current_char in string_input:
        if 'A' <= current_char <= 'Z':
            aggregate_sum += ord(current_char)
    return aggregate_sum