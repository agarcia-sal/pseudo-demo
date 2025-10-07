from typing import List

def compare(scores_game_collection: List[int], guesses_collection: List[int]) -> List[int]:
    result_collection: List[int] = []

    def recursive_iterator(index: int) -> List[int]:
        if index >= len(scores_game_collection):
            return result_collection
        first_element = scores_game_collection[index]
        second_element = guesses_collection[index]
        result_collection.append(abs(first_element - second_element))
        return recursive_iterator(index + 1)

    return recursive_iterator(0)