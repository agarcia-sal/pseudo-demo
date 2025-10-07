from typing import List

def compare(game_scores_collection: List[int], guess_scores_collection: List[int]) -> List[int]:
    def compute_difference(idx: int) -> int:
        first_value = game_scores_collection[idx]
        second_value = guess_scores_collection[idx]
        return first_value - second_value if first_value >= second_value else second_value - first_value

    length_games = len(game_scores_collection)
    result_container: List[int] = []

    index_counter = 0
    while index_counter < length_games:
        result_container.append(compute_difference(index_counter))
        index_counter += 1

    return result_container