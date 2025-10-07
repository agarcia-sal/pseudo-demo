from typing import List


def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> List[int]:
    def helper(idx: int, acc: List[int]) -> List[int]:
        if not (idx < len(list_of_game_scores)):
            return acc
        else:
            return helper(idx + 1, acc + [abs(list_of_game_scores[idx] - list_of_guess_scores[idx])])
    return helper(0, [])