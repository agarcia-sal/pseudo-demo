from typing import List

def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> List[int]:
    differences: List[int] = []
    index: int = 0
    while index < len(list_of_game_scores) and index < len(list_of_guess_scores):
        differences.append(abs(list_of_game_scores[index] - list_of_guess_scores[index]))
        index += 1
    return differences