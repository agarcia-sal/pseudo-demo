from typing import List, NamedTuple

class Query(NamedTuple):
    x: int
    y: int

class Solution:
    def queryResults(self, limit: int, queries: List[Query]) -> List[int]:
        tempMap = {}
        distinctSet = set()
        outputList = []

        for i in range(len(queries)):
            keyVar = queries[i].x
            valVar = queries[i].y

            if keyVar in tempMap:
                prevValue = tempMap[keyVar]
                if prevValue in distinctSet:
                    distinctSet.remove(prevValue)

            tempMap[keyVar] = valVar
            distinctSet.add(valVar)
            outputList.append(len(distinctSet))

        return outputList