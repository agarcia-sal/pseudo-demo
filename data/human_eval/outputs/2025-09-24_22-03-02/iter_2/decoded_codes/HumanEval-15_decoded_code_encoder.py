def string_sequence(n: int) -> str:
    result = ' '.join(str(x) for x in range(n + 1))
    return result