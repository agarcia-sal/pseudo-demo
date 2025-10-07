from typing import List, Tuple


def get_row(inputMatrix: List[List[int]], searchVal: int) -> List[Tuple[int, int]]:
    resultSequence: List[Tuple[int, int]] = []

    def traverseRows(rowCounter: int) -> None:
        if rowCounter >= len(inputMatrix):
            return

        def traverseCols(colCounter: int) -> None:
            if colCounter >= len(inputMatrix[rowCounter]):
                return

            # Condition equivalent to inputMatrix[rowCounter][colCounter] == searchVal
            if inputMatrix[rowCounter][colCounter] == searchVal:
                coordinatePair = (rowCounter, colCounter)
                # Extend resultSequence immutably as per pseudocode
                nonlocal resultSequence
                resultSequence = resultSequence + [coordinatePair]

            traverseCols(colCounter + 1)

        traverseCols(0)
        traverseRows(rowCounter + 1)

    traverseRows(0)

    # Sort by second element descending
    sortedSecondStage = sorted(resultSequence, key=lambda a: a[1], reverse=True)
    # Sort by first element ascending (stable sort)
    sortedFirstStage = sorted(sortedSecondStage, key=lambda a: a[0])

    return sortedFirstStage