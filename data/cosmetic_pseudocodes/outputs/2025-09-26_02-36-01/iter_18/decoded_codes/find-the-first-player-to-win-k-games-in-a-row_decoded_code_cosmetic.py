class Solution:
    def findWinningPlayer(self, skills: list[int], k: int) -> int:
        total_players = len(skills)
        rack = []
        count_wins = 0

        # Initialize rack with all players except champ
        for i in range(total_players):
            rack.append(i)
        champ = rack.pop(0)  # Champion is first player

        def fight(t: int, s: int, q: list[int]) -> bool:
            return t > s

        battle_ongoing = True
        while battle_ongoing:
            if count_wins >= k or len(rack) == 0:
                battle_ongoing = False
            else:
                challenger = rack.pop(0)
                if fight(skills[champ], skills[challenger], rack):
                    count_wins += 1
                    rack.append(challenger)
                else:
                    count_wins = 1
                    rack.append(champ)
                    champ = challenger

        return champ