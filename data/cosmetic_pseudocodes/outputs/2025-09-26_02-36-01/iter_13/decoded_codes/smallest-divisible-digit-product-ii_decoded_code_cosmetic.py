from collections import defaultdict

class Solution:
    FACTOR_COUNTS = {}

    def smallestNumber(self, num: str, t: int) -> str:
        # Initialize FACTOR_COUNTS for digits 0-9 if not done yet
        if not Solution.FACTOR_COUNTS:
            for d in range(10):
                Solution.FACTOR_COUNTS[d] = self._getFactorCount(self._getPrimeCountForNumber(d))

        alpha, omega = self._getPrimeCount(t)
        if not omega:
            return "-1"

        sigma = self._getFactorCount(alpha)
        tau = sum(sigma.values())
        if tau > len(num):
            beta = ""
            for x in sorted(sigma.keys()):
                beta += x * sigma[x]
            return beta

        primeCountPrefix = self.CounterEmpty()
        idx = len(num) - 1
        while idx >= 0:
            self.PrimeCountAdd(primeCountPrefix, Solution.FACTOR_COUNTS[int(num[idx])])
            idx -= 1

        zeroPos = len(num)
        pos = 0
        while pos < len(num):
            if num[pos] == "0":
                zeroPos = pos
                break
            pos += 1

        if zeroPos == len(num) and self.LessEqual(alpha, primeCountPrefix):
            return num

        self._globalResult = None

        def RecursiveSearch(i, prefix):
            if i < 0:
                self.TailReturnValue_Set("")
                return

            d = int(num[i])
            self.PrimeCountSub(prefix, Solution.FACTOR_COUNTS[d])
            spaceAfterThisDigit = len(num) - 1 - i

            if i <= zeroPos:
                digitCandidate = d + 1
                while digitCandidate <= 9:
                    rem = self._getFactorCount(self.SubtractCounter(alpha, prefix, Solution.FACTOR_COUNTS[digitCandidate]))
                    sumRem = sum(rem.values())
                    if sumRem <= spaceAfterThisDigit:
                        onesFill = spaceAfterThisDigit - sumRem
                        prefixStr = self.Substring(num, 0, i) + str(digitCandidate) + self.RepeatChar("1", onesFill)
                        suffixStr = ""
                        for k in sorted(rem.keys()):
                            suffixStr += k * rem[k]
                        self.TailReturnValue_Set(prefixStr + suffixStr)
                        return
                    digitCandidate += 1

            RecursiveSearch(i - 1, prefix)

        RecursiveSearch(len(num) - 1, primeCountPrefix)
        return self.TailReturnValue()

    def TailReturnValue_Set(self, val):
        self._globalResult = val

    def TailReturnValue(self):
        return self._globalResult

    def _getPrimeCount(self, t):
        retCounter = self.CounterEmpty()
        primeList = [2, 3, 5, 7]

        currentVal = t

        def CallFactor(i, val, ctr):
            nonlocal currentVal
            if i == len(primeList):
                currentVal = val
                return
            p = primeList[i]
            while val % p == 0:
                val //= p
                ctr[p] = ctr.get(p, 0) + 1
            CallFactor(i + 1, val, ctr)

        CallFactor(0, currentVal, retCounter)
        return retCounter, (currentVal == 1)

    def _getPrimeCountForNumber(self, number: int) -> dict:
        # Helper to get prime factor counts for a single digit number t
        retCounter = self.CounterEmpty()
        val = number
        for p in [2, 3, 5, 7]:
            while val % p == 0 and val > 1:
                retCounter[p] = retCounter.get(p, 0) + 1
                val //= p
        return retCounter

    def _getFactorCount(self, count: dict) -> dict:
        c2 = self.GetFromCounter(count, 2)
        c3 = self.GetFromCounter(count, 3)
        c5 = self.GetFromCounter(count, 5)
        c7 = self.GetFromCounter(count, 7)

        count8 = self.IntDivision(c2, 3)
        rem2 = c2 % 3
        count9 = self.IntDivision(c3, 2)
        rem3 = c3 % 2

        count4 = self.IntDivision(rem2, 2)
        remCount2 = rem2 % 2

        count2 = 0
        count3 = 0
        count6 = 0
        count4Final = count4

        if remCount2 == 1 and rem3 == 1:
            count2 = 0
            count3 = 0
            count6 = 1
        else:
            count2 = remCount2
            count3 = rem3
            count6 = 0

        if rem3 == 1 and count4Final == 1:
            count2 = 1
            count6 = 1
            count3 = 0
            count4Final = 0

        resultCounter = self.CounterEmpty()
        resultCounter["2"] = count2
        resultCounter["3"] = count3
        resultCounter["4"] = count4Final
        resultCounter["5"] = c5
        resultCounter["6"] = count6
        resultCounter["7"] = c7
        resultCounter["8"] = count8
        resultCounter["9"] = count9
        return resultCounter

    def GetFromCounter(self, counterVar, key):
        return counterVar[key] if key in counterVar else 0

    def IntDivision(self, a, b):
        return (a - (a % b)) // b

    def Modulo(self, a, b):
        return a - b * ((a - (a % b)) // b)

    def CounterEmpty(self):
        return {}

    def PrimeCountAdd(self, counterVar, additionMap):
        for k in additionMap:
            counterVar[k] = counterVar.get(k, 0) + additionMap[k]

    def PrimeCountSub(self, counterVar, subtractionMap):
        for k in subtractionMap:
            counterVar[k] = counterVar.get(k, 0) - subtractionMap[k]

    def LessEqual(self, lhs, rhs):
        for key in lhs:
            lhsVal = lhs[key]
            rhsVal = self.GetFromCounter(rhs, key)
            if lhsVal > rhsVal:
                return False
        return True

    def SubtractCounter(self, a, b, c):
        result = self.CounterEmpty()
        keys = set(a.keys()) | set(b.keys()) | set(c.keys())
        for key in keys:
            aVal = a.get(key, 0)
            bVal = b.get(key, 0)
            cVal = c.get(key, 0)
            val = aVal - bVal - cVal
            if val > 0:
                result[key] = val
        return result

    def RepeatChar(self, ch, n):
        return ch * n if n > 0 else ""

    def Substring(self, s, startInd, endInd):
        return s[startInd:endInd]