from typing import List

def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> List[int]:
    return [abs(gs - gs_guess) for gs, gs_guess in zip(list_of_game_scores, list_of_guess_scores)]