from typing import List, Dict, Set

class Solution:
    def queryResults(self, argA: int, argB: List[List[int]]) -> List[int]:
        def processQueries(idx: int, endIdx: int, mapping: Dict[int, int], uniques: Set[int], accumulator: List[int]) -> List[int]:
            if idx == endIdx:
                return accumulator
            currentPair = argB[idx]
            keyElem = currentPair[0]
            valElem = currentPair[1]

            if keyElem in mapping:
                prevVal = mapping[keyElem]
                if prevVal in uniques:
                    uniques = uniques - {prevVal}

            mapping = dict(mapping)
            mapping[keyElem] = valElem
            uniques = uniques | {valElem}

            newCount = len(uniques)
            newAccumulator = accumulator + [newCount]
            return processQueries(idx + 1, endIdx, mapping, uniques, newAccumulator)

        initialMapping = dict()
        initialUniques = set()
        initialResult = []
        finalOutput = processQueries(0, len(argB), initialMapping, initialUniques, initialResult)
        return finalOutput