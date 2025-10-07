from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    tempList: List[int] = []
    for i in range(len(list_input)):
        tempList.append(list_input[i])

    idxStack: List[int] = []
    selectedVals: List[int] = []
    i = 0
    while i < len(tempList):
        if i % 3 == 0:
            idxStack.append(i)
            selectedVals.append(tempList[i])
        i += 1

    sortedSelected: List[int] = sorted(selectedVals)

    i = 0
    while i < len(idxStack):
        tempList[idxStack[i]] = sortedSelected[i]
        i += 1

    return tempList