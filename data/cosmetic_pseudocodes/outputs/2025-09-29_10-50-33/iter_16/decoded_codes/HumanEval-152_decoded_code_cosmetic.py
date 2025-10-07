from typing import Iterator, List

def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> Iterator[List[int]]:
    paired_scores = zip(list_of_game_scores, list_of_guess_scores)
    differences: List[int] = []
    for score_pair in paired_scores:
        first_score = score_pair[0]
        second_score = score_pair[1]
        difference_value = abs(first_score - second_score)
        differences.append(difference_value)
    yield differences