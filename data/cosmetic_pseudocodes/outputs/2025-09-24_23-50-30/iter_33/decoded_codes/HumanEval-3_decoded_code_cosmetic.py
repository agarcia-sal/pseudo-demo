from typing import Iterable

def below_zero(collection_of_events: Iterable[int]) -> bool:
    accumulator: int = 0
    index: int = 0
    events_list = list(collection_of_events)  # ensure indexing

    while index < len(events_list):
        current_element = events_list[index]
        accumulator += current_element

        if accumulator < 0:
            return True

        index += 1

    return False