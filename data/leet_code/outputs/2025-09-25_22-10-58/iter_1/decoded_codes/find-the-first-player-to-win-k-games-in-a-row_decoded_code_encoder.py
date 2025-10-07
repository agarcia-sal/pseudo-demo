class Solution:
    def findWinningPlayer(self, skills, k):
        n = len(skills)
        from collections import deque
        queue = deque(range(n))
        wins = 0
        current_winner = queue.popleft()
        while wins < k and queue:
            next_player = queue.popleft()
            if skills[current_winner] > skills[next_player]:
                wins += 1
                queue.append(next_player)
            else:
                wins = 1
                queue.append(current_winner)
                current_winner = next_player
        return current_winner