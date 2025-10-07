from collections import deque
from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        queue = deque(range(n))
        current_winner = queue.popleft()
        win_count = 0
        while win_count < k and queue:
            challenger = queue.popleft()
            if skills[current_winner] > skills[challenger]:
                win_count += 1
                queue.append(challenger)
            else:
                win_count = 1
                queue.append(current_winner)
                current_winner = challenger
        return current_winner