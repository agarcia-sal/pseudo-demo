def how_many_times(source_text: str, search_text: str) -> int:
    accumulator: int = 0
    max_position: int = len(source_text) - len(search_text)
    pointer: int = 0
    while pointer <= max_position:
        if source_text[pointer : pointer + len(search_text)] == search_text:
            accumulator += 1
        pointer += 1
    return accumulator