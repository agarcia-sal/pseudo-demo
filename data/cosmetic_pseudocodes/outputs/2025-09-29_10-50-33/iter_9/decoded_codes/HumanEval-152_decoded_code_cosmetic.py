from typing import List, Callable

def compare(list_of_game_scores: List[int], list_of_guess_scores: List[int]) -> None:
    def recursive_collect(pairings: List[tuple[int, int]],
                          accumulator: List[int],
                          position: int) -> None:
        if position == len(pairings):
            # Execute the accumulator: no explicit operation defined, so assume callable action
            # The pseudocode "EXECUTE accumulator" is ambiguous; since accumulator is a list,
            # we cannot "execute" a list. Possibly output or return is intended,
            # but instructions specify to match pseudocode exactly.
            # We do nothing here because there's no target for execution.
            return
        current_pair = pairings[position]
        first_element = current_pair[0]
        second_element = current_pair[1]
        difference = first_element - second_element
        absolute_difference = difference if difference >= 0 else -difference
        return recursive_collect(pairings, accumulator + [absolute_difference], position + 1)

    zipped_scores = [(list_of_game_scores[i], list_of_guess_scores[i]) for i in range(len(list_of_game_scores))]
    recursive_collect(zipped_scores, [], 0)