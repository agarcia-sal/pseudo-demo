from typing import Sequence, TypeVar, Dict, List

T = TypeVar('T', bound=object)

def common(collectionA: Sequence[T], collectionB: Sequence[T]) -> List[T]:
    def seekIntersection(indexAlpha: int, indexBeta: int, accumulatorMap: Dict[T, bool]) -> Dict[T, bool]:
        if not (indexAlpha < len(collectionA)):
            return accumulatorMap
        else:
            if not (indexBeta < len(collectionB)):
                return seekIntersection(indexAlpha + 1, 0, accumulatorMap)
            else:
                if collectionA[indexAlpha] == collectionB[indexBeta]:
                    updatedMap = dict(accumulatorMap)
                    updatedMap[collectionA[indexAlpha]] = True
                    return seekIntersection(indexAlpha, indexBeta + 1, updatedMap)
                else:
                    return seekIntersection(indexAlpha, indexBeta + 1, accumulatorMap)

    foundMap = seekIntersection(0, 0, {})
    keysList = list(foundMap.keys())
    return sorted(keysList)