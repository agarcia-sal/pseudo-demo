def count_upper(string_input: str) -> int:
    count: int = 0
    for ch in string_input:
        if ch.isupper():
            count += 1
    return count