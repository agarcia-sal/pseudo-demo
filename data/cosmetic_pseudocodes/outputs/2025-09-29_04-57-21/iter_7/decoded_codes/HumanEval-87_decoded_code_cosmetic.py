from typing import List, Tuple

def get_row(matrix: List[List[int]], val: int) -> List[Tuple[int, int]]:
    coordinatesList: List[Tuple[int, int]] = []
    outerIdx = 0
    while outerIdx < len(matrix):
        innerIdx = 0
        while innerIdx < len(matrix[outerIdx]):
            if not (matrix[outerIdx][innerIdx] != val):
                coordinatesList.append((outerIdx, innerIdx))
            innerIdx += 1
        outerIdx += 1

    # Sort primarily by row ascending
    coordinatesList.sort(key=lambda a: a[0])
    # Then sort by column descending
    coordinatesList.sort(key=lambda x: x[1], reverse=True)

    return coordinatesList