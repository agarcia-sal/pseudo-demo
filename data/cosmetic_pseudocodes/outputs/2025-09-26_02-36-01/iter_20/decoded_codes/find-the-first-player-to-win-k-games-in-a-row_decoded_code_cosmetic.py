from typing import List, Tuple

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        def popFront(collection: List[int]) -> Tuple[int, List[int]]:
            head = collection[0]
            tail = collection[1:]
            return head, tail

        size = len(skills)

        lineup = list(range(size))

        victory_count = 0
        champion, lineup = popFront(lineup)

        while True:
            if victory_count >= k:
                break
            if not lineup:
                break

            contender, lineup = popFront(lineup)

            champ_skill = skills[champion]
            cont_skill = skills[contender]

            if champ_skill > cont_skill:
                victory_count += 1
                lineup.append(contender)
            else:
                victory_count = 1
                lineup.append(champion)
                champion = contender

        return champion