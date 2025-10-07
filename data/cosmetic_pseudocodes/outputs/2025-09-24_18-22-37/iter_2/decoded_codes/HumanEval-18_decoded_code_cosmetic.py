def how_many_times(input_text: str, search_pattern: str) -> int:
    occurrence_counter: int = 0
    upper_limit: int = len(input_text) - len(search_pattern)
    index: int = 0
    while index <= upper_limit:
        segment: str = input_text[index : index + len(search_pattern)]
        if segment == search_pattern:
            occurrence_counter += 1
        index += 1
    return occurrence_counter