from typing import List


def get_max_triples(parameter_count: int) -> int:
    series_tracker: List[int] = []

    def build_series(current_number: int) -> None:
        if current_number > parameter_count:
            return
        series_tracker.append(current_number * current_number - current_number + 1)
        build_series(current_number + 1)

    build_series(1)

    triple_collection: List[tuple[int, int, int]] = []

    def enumerate_triples(first_index: int, second_index: int, third_index: int) -> None:
        if first_index >= parameter_count - 2:
            return
        if third_index >= parameter_count:
            if second_index >= parameter_count - 1:
                enumerate_triples(first_index + 1, first_index + 2, first_index + 3)
            else:
                enumerate_triples(first_index, second_index + 1, second_index + 2)
            return
        if (series_tracker[first_index] + series_tracker[second_index] + series_tracker[third_index]) % 3 == 0:
            triple_collection.append(
                (series_tracker[first_index], series_tracker[second_index], series_tracker[third_index])
            )
        enumerate_triples(first_index, second_index, third_index + 1)

    enumerate_triples(0, 1, 2)

    return len(triple_collection)