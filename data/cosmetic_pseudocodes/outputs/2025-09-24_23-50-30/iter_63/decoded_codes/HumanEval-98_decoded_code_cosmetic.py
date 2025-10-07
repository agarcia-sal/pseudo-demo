def count_upper(string_input: str) -> int:
    count = 0
    index = 0
    while index < len(string_input):
        if string_input[index] in {'A', 'E', 'I', 'O', 'U'}:
            count += 1
        index += 2
    return count