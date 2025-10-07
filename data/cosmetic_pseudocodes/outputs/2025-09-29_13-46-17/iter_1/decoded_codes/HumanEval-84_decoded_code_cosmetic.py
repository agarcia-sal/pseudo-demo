def solve(integer_N: int) -> str:
    total: int = 0
    string_form: str = str(integer_N)
    for index in range(len(string_form)):
        total += int(string_form[index])
    binary_string: str = bin(total)
    result: str = binary_string[2:]
    return result