from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def helperSortAlpha(betaCoords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def ascendByFirst(vec: List[Tuple[int, int]], pos: int) -> List[Tuple[int, int]]:
            if pos >= len(vec) - 1:
                return vec
            l = vec[pos]
            r = ascendByFirst(vec, pos + 1)
            filtered_ge = [x for x in r if x[0] >= l[0]]
            filtered_lt = [x for x in r if x[0] < l[0]]
            return [l] + filtered_ge + filtered_lt

        def descendBySecond(vec: List[Tuple[int, int]], pos: int) -> List[Tuple[int, int]]:
            if pos >= len(vec) - 1:
                return vec
            l = vec[pos]
            r = descendBySecond(vec, pos + 1)
            filtered_le = [x for x in r if x[1] <= l[1]]
            filtered_gt = [x for x in r if x[1] > l[1]]
            return filtered_le + [l] + filtered_gt

        return ascendByFirst(descendBySecond(betaCoords, 0), 0)

    def gatherCoords(currRow: int, maxRow: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if currRow > maxRow:
            return acc
        def gatherColumns(currCol: int, maxCol: int, accCols: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if currCol > maxCol:
                return accCols
            elem = two_dimensional_list[currRow][currCol]
            accUpdated = accCols + [(currRow, currCol)] if elem == target_integer else accCols
            return gatherColumns(currCol + 1, maxCol, accUpdated)

        rowAccum = gatherColumns(0, len(two_dimensional_list[currRow]) - 1, [])
        return gatherCoords(currRow + 1, maxRow, acc + rowAccum)

    rawCoords = gatherCoords(0, len(two_dimensional_list) - 1, [])
    sortedCoords = helperSortAlpha(rawCoords)
    return sortedCoords