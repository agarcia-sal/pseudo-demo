from typing import List, Tuple


def get_max_triples(num_limit: int) -> int:
    squared_values: List[int] = [(i * i) - i + 1 for i in range(1, num_limit + 1)]
    found_triples: List[Tuple[int, int, int]] = []

    for outer_index in range(num_limit):
        for mid_index in range(outer_index + 1, num_limit):
            for inner_index in range(mid_index + 1, num_limit):
                first_candidate = squared_values[outer_index]
                second_candidate = squared_values[mid_index]
                third_candidate = squared_values[inner_index]
                sum_candidates = first_candidate + second_candidate + third_candidate
                if sum_candidates % 3 == 0:
                    found_triples.append((first_candidate, second_candidate, third_candidate))

    return len(found_triples)