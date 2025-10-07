from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        def locatePositions(collection: List[int], target: int, posList: List[int], idx: int) -> List[int]:
            if idx >= len(collection):
                return posList
            if collection[idx] == target:
                posList.append(idx)
            return locatePositions(collection, target, posList, idx + 1)

        def resolveQueries(queriesList: List[int], posList: List[int], outList: List[int], qIdx: int) -> List[int]:
            if qIdx >= len(queriesList):
                return outList
            currentQuery = queriesList[qIdx]
            if 0 < currentQuery <= len(posList):
                outList.append(posList[currentQuery - 1])
            else:
                outList.append(-1)
            return resolveQueries(queriesList, posList, outList, qIdx + 1)

        foundPositions = locatePositions(nums, x, [], 0)
        responses = resolveQueries(queries, foundPositions, [], 0)
        return responses