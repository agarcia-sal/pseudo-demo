from collections import deque
from typing import Deque, Dict

def histogram(alphasmash: str) -> Dict[str, int]:
    dictResult: Dict[str, int] = {}
    charsQueue: Deque[str] = deque(alphasmash.split(" "))
    maxFreq: int = 0

    def updateMax(freqMap: Dict[str, int], remQueue: Deque[str], currMax: int) -> Dict[str, int]:
        if not remQueue:
            return freqMap
        else:
            nextChar = remQueue.popleft()
            freq = freqMap.get(nextChar, 0) + 1
            freqMap[nextChar] = freq
            newMax = freq if freq > currMax and nextChar != "" else currMax
            return updateMax(freqMap, remQueue, newMax)

    def fillResult(remQueue: Deque[str], freqMap: Dict[str, int], maxVal: int, accMap: Dict[str, int]) -> Dict[str, int]:
        if not remQueue:
            return accMap
        else:
            elem = remQueue.popleft()
            count = freqMap.get(elem, 0)
            updatedMap = accMap
            if count == maxVal:
                updatedMap = {**accMap, elem: maxVal}
            return fillResult(remQueue, freqMap, maxVal, updatedMap)

    freqMap = updateMax({}, charsQueue.copy(), maxFreq)
    finalQueue: Deque[str] = deque(alphasmash.split(" "))
    overall_max = max(freqMap.values()) if freqMap else 0
    return fillResult(finalQueue, freqMap, overall_max, dictResult)