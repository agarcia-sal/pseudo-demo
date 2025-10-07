from typing import List

def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0

    while index_counter < len(list_of_game_scores):
        score_a: int = list_of_game_scores[index_counter]
        score_b: int = list_of_guess_scores[index_counter]
        difference_value: int = score_a - score_b
        if difference_value < 0:
            difference_value = -difference_value
        result_collection.append(difference_value)
        index_counter += 1

    return result_collection