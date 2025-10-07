from typing import List, Tuple

def get_max_triples(input_limit: int) -> int:
    sequence_collection: List[int] = []
    current_index: int = 1
    while current_index <= input_limit:
        computed_value = (current_index * current_index) - current_index + 1
        sequence_collection.append(computed_value)
        current_index += 1

    result_combinations: List[Tuple[int, int, int]] = []

    def explore_combinations(first_cursor: int, second_cursor: int, third_cursor: int) -> None:
        if first_cursor == input_limit - 2:
            return
        if second_cursor == input_limit - 1:
            explore_combinations(first_cursor + 1, first_cursor + 2, first_cursor + 3)
            return
        if third_cursor == input_limit:
            explore_combinations(first_cursor, second_cursor + 1, second_cursor + 2)
            return

        sum_triplet = (
            sequence_collection[first_cursor]
            + sequence_collection[second_cursor]
            + sequence_collection[third_cursor]
        )
        if sum_triplet % 3 == 0:
            result_combinations.append(
                (
                    sequence_collection[first_cursor],
                    sequence_collection[second_cursor],
                    sequence_collection[third_cursor],
                )
            )
        explore_combinations(first_cursor, second_cursor, third_cursor + 1)

    explore_combinations(0, 1, 2)

    return len(result_combinations)