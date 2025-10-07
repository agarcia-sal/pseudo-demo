def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    return sum(ord(c) if 'A' <= c <= 'Z' else 0 for c in string_input)