from typing import List, Tuple

class Solution:
    def findWinningPlayer(self, players_skills: List[int], threshold: int) -> int:
        def dequeue_front(collection: List[int]) -> Tuple[int, List[int]]:
            return collection[0], collection[1:]

        def enqueue_back(collection: List[int], element: int) -> List[int]:
            return collection + [element]

        def play_round(current_champion: int, contenders_list: List[int], consecutive_wins: int) -> int:
            if consecutive_wins >= threshold or len(contenders_list) == 0:
                return current_champion
            challenger, remaining_contenders = dequeue_front(contenders_list)
            if players_skills[current_champion] > players_skills[challenger]:
                updated_consecutive_wins = consecutive_wins + 1
                updated_contenders = enqueue_back(remaining_contenders, challenger)
                return play_round(current_champion, updated_contenders, updated_consecutive_wins)
            else:
                reset_wins = 1
                updated_contenders = enqueue_back(remaining_contenders, current_champion)
                return play_round(challenger, updated_contenders, reset_wins)

        total_players = len(players_skills)
        lineup = []
        idx = 0
        while idx < total_players:
            lineup = lineup + [idx]
            idx += 1

        first_contender, rest_of_contenders = dequeue_front(lineup)
        overall_winner = play_round(first_contender, rest_of_contenders, 0)
        return overall_winner