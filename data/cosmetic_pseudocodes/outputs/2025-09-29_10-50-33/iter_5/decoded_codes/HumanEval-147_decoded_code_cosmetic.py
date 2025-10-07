from typing import List, Tuple

def get_max_triples(number_limit: int) -> int:
    accumulator: List[int] = []
    index_counter: int = 1
    while index_counter <= number_limit:
        computed_value: int = index_counter * index_counter - index_counter + 1
        accumulator.append(computed_value)
        index_counter += 1

    result_collection: List[Tuple[int, int, int]] = []
    primary_cursor: int = 0
    while primary_cursor < number_limit:
        secondary_cursor: int = primary_cursor + 1
        while secondary_cursor < number_limit:
            tertiary_cursor: int = secondary_cursor + 1
            while tertiary_cursor < number_limit:
                if (accumulator[primary_cursor] + accumulator[secondary_cursor] + accumulator[tertiary_cursor]) % 3 == 0:
                    result_collection.append(
                        (accumulator[primary_cursor], accumulator[secondary_cursor], accumulator[tertiary_cursor])
                    )
                tertiary_cursor += 1
            secondary_cursor += 1
        primary_cursor += 1

    return len(result_collection)