class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        baseValue = 10

        def computeModulus() -> int:
            # 10^9 + (3+4) = 10^9 + 7
            return (baseValue ** 9) + (3 + 4)

        modulusValue = computeModulus()
        accumulatedSum = 0

        def absVal(val: int) -> int:
            return val if val >= 0 else -val

        def generateCombinations(elements: list[int], count: int) -> list[list[int]]:
            if count == 0:
                return [[]]
            if not elements:
                return []
            head, tail = elements[0], elements[1:]
            withoutHead = generateCombinations(tail, count)
            withHead = generateCombinations(tail, count - 1)
            for combo in withHead:
                combo.insert(0, head)
            return withoutHead + withHead

        combosList = generateCombinations(nums, k)
        comboIndex = 0

        while comboIndex < len(combosList):
            selectedCombo = combosList[comboIndex]

            # 10^9
            largeNumber = 10 ** 9

            minimumDiff = largeNumber + largeNumber  # effectively a large value: 2 * 10^9

            outerLoopIndex = 0
            while outerLoopIndex <= (k - 1):
                innerLoopIndex = outerLoopIndex + 1
                while innerLoopIndex <= (k - 1):
                    firstVal = selectedCombo[outerLoopIndex]
                    secondVal = selectedCombo[innerLoopIndex]
                    diffCandidate = absVal(firstVal - secondVal)
                    if diffCandidate < minimumDiff:
                        minimumDiff = diffCandidate
                    innerLoopIndex += 1
                outerLoopIndex += 1

            accumulatedSum += minimumDiff
            # Modular reduction
            accumulatedSum = accumulatedSum - ((accumulatedSum // modulusValue) * modulusValue)

            comboIndex += 1

        return accumulatedSum