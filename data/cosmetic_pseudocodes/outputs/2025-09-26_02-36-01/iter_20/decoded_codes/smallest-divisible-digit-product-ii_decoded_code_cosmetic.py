from collections import Counter

class Solution:
    def smallestNumber(self, number: str, flag: int) -> str:
        def wrapperAlpha(gamma):
            delta = Counter()
            beta = 0

            def loopEpsilon(theta):
                nonlocal beta
                while theta % gamma[beta] == 0:
                    theta //= gamma[beta]
                    delta[gamma[beta]] += 1
                beta += 1

            while beta < 4:
                loopEpsilon(flag)

            return delta, (flag == 1)

        def helperBeta(epsilon: Counter):
            # Access values with default 0 if not present
            def get_count(k):
                return epsilon.get(k, 0)

            xi = get_count(2) // 3
            rho = get_count(2) % 3
            phi = get_count(3) // 2
            chi = get_count(3) % 2
            psi = rho // 2
            omega = rho % 2
            tau = 0

            if omega == 1 and chi == 1:
                omega = 0
                chi = 0
                tau = 1
            else:
                tau = 0

            if chi == 1 and psi == 1:
                omega = 1
                tau = 1
                chi = 0
                psi = 0

            return Counter({
                '2': omega,
                '3': chi,
                '4': psi,
                '5': get_count(5),
                '6': tau,
                '7': get_count(7),
                '8': xi,
                '9': phi
            })

        lambda_counter, mu = wrapperAlpha(flag)
        if not mu:
            return "-1"
        nu = helperBeta(lambda_counter)

        sigma = 0
        kappa = Counter()
        iota = len(number)

        for char in number:
            digit = int(char)
            kappa += helperBeta(Counter({digit: 1}))

        for value in kappa.values():
            sigma += value

        if sigma > iota:
            resultString = ""
            for key, value in nu.items():
                resultString += key * value
            return resultString

        zeta = 0
        pos = 0
        while True:
            if pos >= iota:
                break
            if number[pos] == '0':
                zeta = pos
                pos = iota
            else:
                pos += 1

        if zeta == iota and all(lambda_counter.get(k, 0) <= kappa.get(k, 0) for k in lambda_counter):
            return number

        sumHolder = 0

        def minusCounters(mainCounter: Counter, subCounter: Counter) -> Counter:
            newCounter = Counter()
            keys = set(mainCounter.keys()).union(subCounter.keys())
            for key in keys:
                newCounter[key] = mainCounter.get(key, 0) - subCounter.get(key, 0)
            return newCounter

        cumulativeCounter = Counter()
        for j in range(iota - 1, -1, -1):
            digitChar = number[j]
            digitNum = int(digitChar)
            deltaCounter = helperBeta(Counter({digitNum: 1}))
            for pKey, pVal in deltaCounter.items():
                cumulativeCounter[pKey] = cumulativeCounter.get(pKey, 0) + pVal

        recursionIndex = iota - 1

        def runLoop():
            nonlocal recursionIndex
            if recursionIndex < 0:
                return None
            charAtIndex = number[recursionIndex]
            digitValue = int(charAtIndex)
            subtractCounter = helperBeta(Counter({digitValue: 1}))
            for k in subtractCounter:
                cumulativeCounter[k] = cumulativeCounter.get(k, 0) - subtractCounter[k]
            spaceRem = len(number) - 1 - recursionIndex
            if recursionIndex <= zeta:
                for numX in range(digitValue + 1, 10):
                    # Calculate trialCounter = lambda - cumulativeCounter
                    trialCounter = minusCounters(lambda_counter, cumulativeCounter)
                    numX_str = str(numX)
                    if numX_str not in trialCounter:
                        trialCounter[numX_str] = 0
                    # Subtract helperBeta of numX digit itself from trialCounter
                    # Note: helperBeta expects Counter with int keys, but trialCounter keys are strings
                    # We'll convert trialCounter's string keys to ints where needed for helperBeta input
                    # Let's build Counter input for helperBeta for numX digit
                    trialCounter_for_helper = Counter()
                    # trialCounter keys are strings representing digits, helperBeta expects Counter with int keys
                    for k, v in trialCounter.items():
                        trialCounter_for_helper[int(k)] = v
                    trialCounter2 = helperBeta(minusCounters(trialCounter_for_helper, helperBeta(Counter({numX: 1}))))
                    totalVals = sum(trialCounter2.values())
                    if totalVals <= spaceRem:
                        fillCount = spaceRem - totalVals
                        part1 = number[:recursionIndex]
                        part2 = str(numX)
                        part3 = "1" * fillCount
                        part4 = ""
                        # trialCounter2 keys are strings, values are counts
                        # Add all keys repeated by their counts
                        for keyQ, valQ in sorted(trialCounter2.items()):
                            part4 += keyQ * valQ
                        return part1 + part2 + part3 + part4
            recursionIndex -= 1
            return runLoop()

        outcome = runLoop()
        if outcome is not None:
            return outcome

        deltaFinal = helperBeta(lambda_counter)
        finalLength = len(number) + 1
        countSumFinal = sum(deltaFinal.values())
        frontPart = "1" * (finalLength - countSumFinal)
        backPart = ""
        for keyY, valY in sorted(deltaFinal.items()):
            backPart += keyY * valY
        return frontPart + backPart