from typing import Union

def how_many_times(text_data: Union[str, bytes], search_term: Union[str, bytes]) -> int:
    result_counter: int = 0
    position: int = 0
    max_start: int = len(text_data) - len(search_term)
    while position <= max_start:
        slice_start: int = position
        slice_end: int = slice_start + len(search_term)
        segment = text_data[slice_start:slice_end]
        if segment == search_term:
            result_counter += 1
        position += 1
    return result_counter