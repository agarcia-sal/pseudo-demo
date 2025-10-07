def count_upper(string_input: str) -> int:
    total_hits = 0
    idx = 0

    while idx < len(string_input):
        if idx % 2 == 0:
            if string_input[idx] in {"A", "E", "I", "O", "U"}:
                total_hits += 1
        idx += 1

    return total_hits