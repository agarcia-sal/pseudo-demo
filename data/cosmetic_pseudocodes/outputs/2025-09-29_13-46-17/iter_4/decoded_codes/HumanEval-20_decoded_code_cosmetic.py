from typing import List, Optional, Tuple


def find_closest_elements(Nums_list: List[int]) -> Optional[Tuple[int, int]]:
    nearest: Optional[Tuple[int, int]] = None
    mindiff: Optional[int] = None

    pix = 0
    while pix < len(Nums_list) - 1:
        agent = Nums_list[pix]
        runner = 0
        while runner < len(Nums_list) - 1:
            contender = Nums_list[runner]
            if pix != runner:
                candidate_diff = abs(agent - contender)
                if mindiff is None or candidate_diff < mindiff:
                    mindiff = candidate_diff
                    nearest = (min(agent, contender), max(agent, contender))
            runner += 1
        pix += 1

    return nearest