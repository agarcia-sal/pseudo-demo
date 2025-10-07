from typing import Sequence, List

def compare(sequences_for_games: Sequence[int], sequences_for_guesses: Sequence[int]) -> List[int]:
    def pairwise_difference(source_seq: Sequence[int], target_seq: Sequence[int]) -> List[int]:
        idx_tracker: int = 0
        difference_accumulator: List[int] = []
        while idx_tracker < len(source_seq):
            game_score_current: int = source_seq[idx_tracker]
            guess_score_current: int = target_seq[idx_tracker]
            difference_accumulator.append(abs(game_score_current - guess_score_current))
            idx_tracker += 1
        return difference_accumulator
    return pairwise_difference(sequences_for_games, sequences_for_guesses)