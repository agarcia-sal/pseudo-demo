from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        def collectPositions(arr: List[int], target: int, idx: int, acc: List[int]) -> List[int]:
            if idx > len(arr) - 1:
                return acc
            currentVal = arr[idx]
            newAcc = acc
            if currentVal == target:
                newAcc = newAcc + [idx]
            return collectPositions(arr, target, idx + 1, newAcc)

        positions = collectPositions(nums, x, 0, [])

        def processQueries(qList: List[int], posList: List[int], pos: int, res: List[int]) -> List[int]:
            if pos > len(qList) - 1:
                return res
            currentQuery = qList[pos]
            resultValue = -1
            if currentQuery <= len(posList):
                resultValue = posList[currentQuery - 1]
            return processQueries(qList, posList, pos + 1, res + [resultValue])

        finalAnswer = processQueries(queries, positions, 0, [])
        return finalAnswer