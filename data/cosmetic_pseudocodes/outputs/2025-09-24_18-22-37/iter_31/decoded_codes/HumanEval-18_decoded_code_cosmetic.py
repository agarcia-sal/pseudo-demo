def how_many_times(source_text: str, search_text: str) -> int:
    match_tally = 0
    max_start = len(source_text) - len(search_text)
    current_pos = 0
    while current_pos <= max_start:
        segment = source_text[current_pos : current_pos + len(search_text)]
        if segment == search_text:
            match_tally += 1
        current_pos += 1
    return match_tally