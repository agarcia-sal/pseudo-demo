def how_many_times(some_string: str, search_string: str) -> int:
    count_accumulator: int = 0
    position_marker: int = 0
    termination_point: int = len(some_string) - len(search_string)
    while position_marker <= termination_point:
        extracted_segment = some_string[position_marker : position_marker + len(search_string)]
        if extracted_segment == search_string:
            count_accumulator += 1
        position_marker += 1
    return count_accumulator