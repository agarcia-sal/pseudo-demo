from collections import deque

class Solution:
    def findWinningPlayer(self, skills, k):
        total_players = len(skills)
        lineup = deque()
        index_counter = 0

        while index_counter < total_players:
            lineup.append(index_counter)
            index_counter += 1

        winning_streak = 0
        leader = lineup.popleft()

        while winning_streak < k and len(lineup) > 0:
            challenger = lineup.popleft()
            leader_skill = skills[leader]
            challenger_skill = skills[challenger]

            if leader_skill > challenger_skill:
                winning_streak += 1
                lineup.append(challenger)
            else:
                winning_streak = 1
                lineup.append(leader)
                leader = challenger

        return leader