from typing import List, Optional

def can_arrange(inputList: List[int]) -> int:
    marker: int = -1
    position: int = 0

    def traverse(nextPos: int) -> None:
        nonlocal marker
        if not (nextPos < len(inputList)):
            return
        if inputList[nextPos] < inputList[nextPos - 1]:
            marker = nextPos
        traverse(nextPos + 1)

    traverse(position + 1)
    return marker