from typing import Sequence, List, Dict, TypeVar

T = TypeVar('T')

def sort_third(container: Sequence[T]) -> List[T]:
    backupList: List[T] = []
    idxSequence: int = 0
    while idxSequence < len(container):
        backupList.append(container[idxSequence])
        idxSequence += 1

    subsetMap: Dict[int, T] = {}
    posCursor: int = 0
    while True:
        if posCursor >= len(backupList):
            break
        subsetMap[posCursor] = backupList[posCursor]
        posCursor += 3

    sortedSubset: List[T] = []
    for keyValue in subsetMap.items():
        sortedSubset.append(keyValue[1])
    sortedSubset.sort()

    replaceIndex: int = 0
    for key in subsetMap.keys():
        backupList[key] = sortedSubset[replaceIndex]
        replaceIndex += 1

    return backupList