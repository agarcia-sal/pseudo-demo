def how_many_times(main_text: str, seek_text: str) -> int:
    total_found: int = 0
    pos: int = 0
    end: int = len(main_text) - len(seek_text)
    while pos <= end:
        if main_text[pos : pos + len(seek_text)] == seek_text:
            total_found += 1
        pos += 1
    return total_found