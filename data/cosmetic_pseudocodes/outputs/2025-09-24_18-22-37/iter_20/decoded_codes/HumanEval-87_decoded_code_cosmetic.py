from typing import List, Tuple


def get_row(matrix: List[List[int]], value: int) -> List[Tuple[int, int]]:
    foundPositions: List[Tuple[int, int]] = []
    outerIndex = 0
    while outerIndex < len(matrix):
        innerIndex = 0
        row = matrix[outerIndex]
        while innerIndex < len(row):
            element = row[innerIndex]
            if element == value:
                foundPositions.append((outerIndex, innerIndex))
            innerIndex += 1
        outerIndex += 1

    tempPositions = foundPositions

    sortedListDescending: List[Tuple[int, int]] = []
    descendingIndex = 0
    while descendingIndex < len(tempPositions):
        sortedListDescending.append(tempPositions[descendingIndex])
        descendingIndex += 1

    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < len(sortedListDescending) - 1:
            current = sortedListDescending[i]
            next_ = sortedListDescending[i + 1]
            if current[1] < next_[1]:
                # swap elements to have descending order by second element
                sortedListDescending[i], sortedListDescending[i + 1] = next_, current
                swapped = True
            i += 1

    finalList: List[Tuple[int, int]] = sortedListDescending[:]
    sortedIndex = 0
    while sortedIndex < len(finalList):
        finalList.append(finalList[sortedIndex])
        sortedIndex += 1

    swapped = True
    while swapped:
        swapped = False
        j = 0
        while j < len(finalList) - 1:
            curr = finalList[j]
            nxt = finalList[j + 1]
            if curr[0] > nxt[0]:
                finalList[j], finalList[j + 1] = nxt, curr
                swapped = True
            j += 1

    return finalList