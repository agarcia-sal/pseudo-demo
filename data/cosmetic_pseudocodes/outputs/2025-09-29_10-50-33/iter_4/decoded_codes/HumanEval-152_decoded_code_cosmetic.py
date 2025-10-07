from typing import Iterable, List, Tuple

def compare(scores_games_collection: Iterable[float], recorded_guess_values: Iterable[float]) -> List[float]:
    # Compute the absolute differences between corresponding elements of the two iterables
    return [abs(item_b - item_a) for item_a, item_b in zip(recorded_guess_values, scores_games_collection)]