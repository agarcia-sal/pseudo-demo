from typing import List, Set, Tuple


def get_max_triples(n_count: int) -> int:
    def generate_series(current_pos: int, accumulator: List[int]) -> None:
        if current_pos <= n_count:
            accumulator.append(current_pos * current_pos - current_pos + 1)
            generate_series(current_pos + 1, accumulator)

    series_collection: List[int] = []
    generate_series(1, series_collection)

    def collect_valid_triplets(
        first_idx: int, second_idx: int, third_idx: int, results: Set[Tuple[int, int, int]]
    ) -> None:
        if first_idx >= n_count - 2:
            return
        elif second_idx >= n_count - 1:
            collect_valid_triplets(first_idx + 1, first_idx + 2, first_idx + 3, results)
        elif third_idx >= n_count:
            collect_valid_triplets(first_idx, second_idx + 1, second_idx + 2, results)
        else:
            s = series_collection[first_idx] + series_collection[second_idx] + series_collection[third_idx]
            if s % 3 == 0:
                results.add(
                    (
                        series_collection[first_idx],
                        series_collection[second_idx],
                        series_collection[third_idx],
                    )
                )
            collect_valid_triplets(first_idx, second_idx, third_idx + 1, results)

    triples_found: Set[Tuple[int, int, int]] = set()
    collect_valid_triplets(0, 1, 2, triples_found)
    return len(triples_found)