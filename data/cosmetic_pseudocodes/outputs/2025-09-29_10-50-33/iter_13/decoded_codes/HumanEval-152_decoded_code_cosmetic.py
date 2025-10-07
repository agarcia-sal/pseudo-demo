from typing import List

def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> List[int]:
    result_differences: List[int] = []
    index_counter: int = 0

    while True:
        if not (index_counter < len(list_of_game_scores)):
            return result_differences[::-1]
        game_score: int = list_of_game_scores[index_counter]
        guess_score: int = list_of_guess_scores[index_counter]
        result_differences.insert(0, abs(game_score - guess_score))
        index_counter += 1