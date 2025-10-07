def string_sequence(integer_n: int) -> str:
    result: list[str] = []
    for number in range(integer_n + 1):
        result.append(str(number))
    return " ".join(result)