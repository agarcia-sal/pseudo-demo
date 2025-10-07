from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def findMatches(
        rowList: List[List[int]],
        tgt: int,
        rowIdx: int,
        colIdx: int,
        foundCoords: List[Tuple[int, int]],
    ) -> List[Tuple[int, int]]:
        if rowIdx == len(rowList):
            return foundCoords
        if colIdx == len(rowList[rowIdx]):
            return findMatches(rowList, tgt, rowIdx + 1, 0, foundCoords)

        currentVal = rowList[rowIdx][colIdx]
        updatedCoords = foundCoords
        if currentVal == tgt:
            updatedCoords = foundCoords + [(rowIdx, colIdx)]
        return findMatches(rowList, tgt, rowIdx, colIdx + 1, updatedCoords)

    def sortBySecondDesc(
        coords: List[Tuple[int, int]], sorted_list: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        if not coords:
            return sorted_list

        maxPair = coords[0]
        restPairs = coords[1:]
        # Find pair with max second element
        for itm in restPairs:
            if itm[1] > maxPair[1]:
                maxPair = itm
        filteredRest = [p for p in restPairs if p != maxPair]
        return sortBySecondDesc(filteredRest, sorted_list + [maxPair])

    def sortByFirstAsc(
        coords: List[Tuple[int, int]], sorted_list: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        if not coords:
            return sorted_list

        minPair = coords[0]
        restPairs = coords[1:]
        # Find pair with min first element
        for itm in restPairs:
            if itm[0] < minPair[0]:
                minPair = itm
        filteredRest = [p for p in restPairs if p != minPair]
        return sortByFirstAsc(filteredRest, sorted_list + [minPair])

    initialCoords: List[Tuple[int, int]] = []
    collectedCoords = findMatches(two_dimensional_list, target_integer, 0, 0, initialCoords)
    coordsSortedBySecondDesc = sortBySecondDesc(collectedCoords, [])
    coordsSortedByFirstAsc = sortByFirstAsc(coordsSortedBySecondDesc, [])
    return coordsSortedByFirstAsc