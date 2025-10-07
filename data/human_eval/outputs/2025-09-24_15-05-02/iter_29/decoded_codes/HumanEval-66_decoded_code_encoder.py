def digitSum(input_string: str) -> int:
    if input_string == "":
        return 0
    return sum(ord(c) if c.isupper() else 0 for c in input_string)