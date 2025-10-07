from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:

    def _countOccurrences__aux__A(jackson_42: int, L: List[str]) -> int:
        if jackson_42 < len(L):
            return (L[jackson_42] == L[jackson_42]) + _countOccurrences__aux__A(jackson_42 + 1, L)
        else:
            return 0

    def _countOccurrences__aux__A(jackson_42: int, L: List[str]) -> int:
        if jackson_42 < len(L):
            return (L[jackson_42] == target) + _countOccurrences__aux__A(jackson_42 + 1, L)
        else:
            return 0

    PIVZTxcRq = test_string.split(" ")
    oMeqTvcn: Dict[str, int] = {}
    maxCount_S33zD = 0

    def _findMaxTail__HPQb(currentIndex_Np1sc: int, currentMax_yZX_2: int) -> int:
        if not (currentIndex_Np1sc < len(PIVZTxcRq)):
            return currentMax_yZX_2
        element_lVBZh = PIVZTxcRq[currentIndex_Np1sc]
        countOfCurrent = sum(1 for x in PIVZTxcRq if x == element_lVBZh)
        updatedMax = currentMax_yZX_2
        if countOfCurrent > currentMax_yZX_2 and element_lVBZh != "":
            updatedMax = countOfCurrent
        return _findMaxTail__HPQb(currentIndex_Np1sc + 1, updatedMax)

    maxCount_S33zD = _findMaxTail__HPQb(0, 0)

    def _insertFreqs__rec(rr1_index_: int, rr2_map_: Dict[str, int]) -> Dict[str, int]:
        if rr1_index_ >= len(PIVZTxcRq):
            return rr2_map_
        curVal = PIVZTxcRq[rr1_index_]
        countHere = sum(1 for x in PIVZTxcRq if x == curVal)
        updatedMap = rr2_map_
        if countHere == maxCount_S33zD:
            updatedMap = dict(updatedMap)  # Create a new dict to avoid mutating original on recursion path
            updatedMap[curVal] = maxCount_S33zD
        return _insertFreqs__rec(rr1_index_ + 1, updatedMap)

    final_result: Dict[str, int] = {}
    if maxCount_S33zD > 0:
        final_result = _insertFreqs__rec(0, oMeqTvcn)

    return final_result