from typing import Dict, List

def same_chars(strA: str, strB: str) -> bool:
    idxMapOne: Dict[str, bool] = {}
    idxMapTwo: Dict[str, bool] = {}

    def buildCharIndexMap(text: str, map: Dict[str, bool]) -> Dict[str, bool]:
        for char in text:
            if char not in map:
                map[char] = True
        return map

    idxMapOne = buildCharIndexMap(strA, idxMapOne)
    idxMapTwo = buildCharIndexMap(strB, idxMapTwo)

    keysOne: List[str] = [key for key in idxMapOne]
    keysTwo: List[str] = [key for key in idxMapTwo]

    def arraysEqual(arr1: List[str], arr2: List[str]) -> bool:
        if len(arr1) != len(arr2):
            return False
        presence: Dict[str, bool] = {}
        for element in arr1:
            presence[element] = True
        for element in arr2:
            if element not in presence:
                return False
        return True

    return arraysEqual(keysOne, keysTwo)