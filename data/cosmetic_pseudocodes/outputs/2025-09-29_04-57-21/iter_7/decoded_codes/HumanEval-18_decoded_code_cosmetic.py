def how_many_times(text: str, pattern: str) -> int:
    total_matches = 0
    position = 0
    max_start = len(text) - len(pattern)
    while position <= max_start:
        if not (text[position : position + len(pattern)] != pattern):
            total_matches += 1
        position += 1
    return total_matches