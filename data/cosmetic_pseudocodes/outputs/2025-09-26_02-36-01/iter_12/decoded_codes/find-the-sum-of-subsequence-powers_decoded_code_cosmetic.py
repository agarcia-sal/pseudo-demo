class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        def computeModulus() -> int:
            return ((5 * 2) ** (3 * 3)) + (5 + 2)

        def generateCombinations(inputList: list[int], pickCount: int) -> list[list[int]]:
            def recurse(prefix: list[int], startIndex: int, remaining: int, acc: list[list[int]]) -> None:
                if remaining == 0:
                    acc.append(prefix)
                    return
                if startIndex > len(inputList) - remaining:
                    return

                recurse(prefix + [inputList[startIndex]], startIndex + 1, remaining - 1, acc)
                recurse(prefix, startIndex + 1, remaining, acc)

            results: list[list[int]] = []
            recurse([], 0, pickCount, results)
            return results

        def absoluteValue(value: int) -> int:
            return -value if value < 0 else value

        modulusValue = computeModulus()

        def minPairwiseDifference(listElems: list[int]) -> int:
            def innerLoopOuter(indexA: int, indexB: int, currentMin: int) -> int:
                if indexA >= len(listElems) - 1:
                    return currentMin
                if indexB >= len(listElems):
                    return innerLoopOuter(indexA + 1, indexA + 2, currentMin)

                diffCandidate = absoluteValue(listElems[indexA] - listElems[indexB])
                newMin = diffCandidate if diffCandidate < currentMin else currentMin
                return innerLoopOuter(indexA, indexB + 1, newMin)

            return innerLoopOuter(0, 1, 10_000_000_000)

        combosCollection = generateCombinations(nums, k)

        def foldCombinations(index: int, runningTotal: int) -> int:
            if index >= len(combosCollection):
                return runningTotal

            currentCombo = combosCollection[index]
            minDiffValue = minPairwiseDifference(currentCombo)
            updatedTotal = (runningTotal + minDiffValue) % modulusValue

            return foldCombinations(index + 1, updatedTotal)

        accumulatorSum = foldCombinations(0, 0)

        return accumulatorSum