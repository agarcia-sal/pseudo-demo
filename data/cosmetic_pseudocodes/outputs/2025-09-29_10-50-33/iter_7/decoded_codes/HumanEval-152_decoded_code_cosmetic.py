from typing import List

def compare(scoreboard_games: List[int], scoreboard_guesses: List[int]) -> List[int]:
    def compute_differences(
        cursor_games: List[int], cursor_guesses: List[int], accumulated_results: List[int]
    ) -> List[int]:
        if not cursor_games or not cursor_guesses:
            return accumulated_results
        head_game = cursor_games[0]
        head_guess = cursor_guesses[0]
        difference = head_game - head_guess
        magnitude = -difference if difference < 0 else difference
        accumulated_results.append(magnitude)
        return compute_differences(cursor_games[1:], cursor_guesses[1:], accumulated_results)

    return compute_differences(scoreboard_games, scoreboard_guesses, [])