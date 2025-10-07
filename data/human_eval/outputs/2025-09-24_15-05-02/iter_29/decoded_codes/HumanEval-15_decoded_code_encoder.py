def string_sequence(integer_n: int) -> str:
    if integer_n < 0:
        return ""
    return " ".join(str(i) for i in range(integer_n + 1))