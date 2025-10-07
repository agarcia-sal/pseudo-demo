class Solution:
    FACTOR_COUNTS = {
        0: {},
        1: {},
        2: {"2": 1},
        3: {"3": 1},
        4: {"2": 2},
        5: {"5": 1},
        6: {"3": 1, "2": 1},
        7: {"7": 1},
        8: {"2": 3},
        9: {"3": 2}
    }

    def smallestNumber(self, num: str, t: int) -> str:
        primeFactors, divisibleFlag = self._getPrimeCount(t)
        if not divisibleFlag:
            return "-1"

        factorDistribution = self._getFactorCount(primeFactors)
        factorSum = sum(factorDistribution.values())

        if factorSum > len(num):
            assembledString = "".join(
                key * freq for key, freq in sorted(factorDistribution.items())
            )
            return assembledString

        def sumFactorsInNum(index: int, accumCounter: dict) -> dict:
            if index == len(num):
                return accumCounter
            digitVal = int(num[index])
            updatedCounter = accumCounter.copy()
            for factorKey, val in self.FACTOR_COUNTS[digitVal].items():
                updatedCounter[factorKey] = updatedCounter.get(factorKey, 0) + val
            return sumFactorsInNum(index + 1, updatedCounter)

        prefixFactors = sumFactorsInNum(0, {})

        def findFirstZeroPos(pos: int, bound: int) -> int:
            # Recursive find zero position or bound if none found
            if pos == bound:
                return bound
            if num[pos] == "0":
                return pos
            return findFirstZeroPos(pos + 1, bound)

        zeroIndex = findFirstZeroPos(0, len(num))

        # Check if num already satisfies conditions
        if zeroIndex == len(num):
            for k, v in primeFactors.items():
                if v > prefixFactors.get(k, 0):
                    break
            else:
                return num

        def processDigitReverse(i: int, prefixCounter: dict) -> str | None:
            if i < 0:
                return None

            currentDigit = int(num[i])
            updatedPrefixCounter = prefixCounter.copy()
            for key, val in self.FACTOR_COUNTS[currentDigit].items():
                updatedPrefixCounter[key] = updatedPrefixCounter.get(key, 0) - val

            remainingSpaces = len(num) - 1 - i

            if i <= zeroIndex:
                for candidateDigit in range(currentDigit + 1, 10):
                    diffCounter = {}
                    for k in primeFactors.keys():
                        diffCounter[k] = primeFactors[k] - updatedPrefixCounter.get(k, 0) - self.FACTOR_COUNTS.get(candidateDigit, {}).get(k, 0)
                    replacementFactors = self._getFactorCount(diffCounter)
                    sumReplacement = sum(replacementFactors.values())
                    if sumReplacement <= remainingSpaces:
                        onesToInsert = remainingSpaces - sumReplacement
                        leftPart = num[:i] if i > 0 else ""
                        middlePart = str(candidateDigit)
                        onesPart = "1" * onesToInsert
                        rightPart = "".join(
                            f * count
                            for f, count in sorted(replacementFactors.items())
                        )
                        return leftPart + middlePart + onesPart + rightPart

            return processDigitReverse(i - 1, updatedPrefixCounter)

        answer = processDigitReverse(len(num) - 1, prefixFactors)
        if answer is not None:
            return answer

        finalFactorCount = self._getFactorCount(primeFactors)
        finalSum = sum(finalFactorCount.values())
        onesString = "1" * (len(num) + 1 - finalSum)
        tailString = "".join(
            key * freq for key, freq in sorted(finalFactorCount.items())
        )
        return onesString + tailString

    def _getPrimeCount(self, t: int) -> tuple[dict[int, int], bool]:
        cntMap = {}
        primesList = [2, 3, 5, 7]

        def factorCountRec(value: int, idx: int) -> tuple[int, dict[int, int]]:
            if idx == len(primesList):
                return value, cntMap
            currentPrime = primesList[idx]
            if value % currentPrime == 0:
                cntMap[currentPrime] = cntMap.get(currentPrime, 0) + 1
                return factorCountRec(value // currentPrime, idx)
            else:
                return factorCountRec(value, idx + 1)

        remaining, counts = factorCountRec(t, 0)
        return counts, (remaining == 1)

    def _getFactorCount(self, counts: dict[int, int]) -> dict[str, int]:
        twoCount = counts.get(2, 0)
        threeCount = counts.get(3, 0)
        fiveCount = counts.get(5, 0)
        sevenCount = counts.get(7, 0)

        twoCountDiv3 = twoCount // 3
        twoCountMod3 = twoCount % 3
        threeCountDiv2 = threeCount // 2
        threeCountMod2 = threeCount % 2
        fourCountDiv2 = twoCountMod3 // 2
        fourCountMod2 = twoCountMod3 % 2

        aCount2 = fourCountMod2
        aCount3 = threeCountMod2
        sixCount = 0

        if aCount2 == 1 and aCount3 == 1:
            aCount2 = 0
            aCount3 = 0
            sixCount = 1

        if aCount3 == 1 and fourCountDiv2 == 1:
            aCount2 = 1
            sixCount = 1
            aCount3 = 0
            fourCountDiv2 = 0

        return {
            "2": aCount2,
            "3": aCount3,
            "4": fourCountDiv2,
            "5": fiveCount,
            "6": sixCount,
            "7": sevenCount,
            "8": twoCountDiv3,
            "9": threeCountDiv2
        }