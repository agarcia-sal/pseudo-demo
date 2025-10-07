from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeFactors, divisibleFlag = self._getPrimeCount(t)
        if not divisibleFlag:
            return "-1"

        factorFreqs = self._getFactorCount(primeFactors)
        if sum(factorFreqs.values()) > len(num):
            resultStr = ""
            for digit in sorted(factorFreqs.keys()):
                resultStr += digit * factorFreqs[digit]
            return resultStr

        def sum_factor_counts(digit: int) -> int:
            # Helper: sum of factor counts of a single digit
            return sum(self._getFactorCount(self._getPrimeCount(digit)[0]).values())

        prefixPrimeSum = 0
        for ch in num:
            prefixPrimeSum += sum_factor_counts(int(ch))

        zeroIdx = len(num)
        position = 0
        while position < len(num) and num[position] != "0":
            position += 1
        if position < len(num):
            zeroIdx = position

        # If no zeros found and primeFactors are less or equal prefixPrimeSum
        # return num directly
        # The condition primeFactors <= prefixPrimeSum is checked by comparing sums of values
        if zeroIdx == len(num):
            if sum(primeFactors.values()) <= prefixPrimeSum:
                return num

        prefixSum = prefixPrimeSum
        for pos in range(len(num) - 1, -1, -1):
            currentDigit = int(num[pos])
            prefixSum -= sum_factor_counts(currentDigit)
            availableSpace = len(num) - 1 - pos
            if pos <= zeroIdx:
                candidateDigit = currentDigit + 1
                while candidateDigit <= 9:
                    remaining = primeFactors.copy()
                    # Decrease counts from prefixSum and candidateDigit factor counts
                    # Calculate new factor counts needed for (primeFactors - prefixSum - factors(candidateDigit))
                    # Actually we consider the factor counts of (primeFactors - prefixSum - factorCounts(candidateDigit)),
                    # but since factorFreqs works on Counters of primeFactors,
                    # we'll subtract Counters and check if possible.
                    candidate_factors = self._getFactorCount(Counter(primeFactors) - Counter({}) )  # Placeholder to help typing
                    # Instead of direct arithmetic with factorFreqs, we do counter arithmetic:

                    # first calculate the remaining prime factor counts needed after adding candidateDigit
                    required_factors = Counter()
                    # primeFactors (Counter) - (prefixSum + factorCounts(candidateDigit))
                    # Actually prefixSum is sum of factor counts of prefix digits,
                    # but factorFreqs uses primeFactors Counter. To handle easily,
                    # we convert prefixSum and candidateDigit factor count to Counters first

                    # So we need a function to get prime factor counts of a digit:
                    digit_pf_counts = self._getPrimeCount(candidateDigit)[0]

                    needed_pf_counts = primeFactors - self._counter_from_sum(prefixSum) - digit_pf_counts
                    if any(v < 0 for v in needed_pf_counts.values()):
                        candidateDigit += 1
                        continue

                    changeFactors = self._getFactorCount(needed_pf_counts)
                    changeSum = sum(changeFactors.values())
                    if changeSum <= availableSpace:
                        onesCount = availableSpace - changeSum
                        prefix_part = num[:pos]
                        ans = prefix_part + str(candidateDigit) + "1" * onesCount
                        for d in sorted(changeFactors.keys()):
                            ans += d * changeFactors[d]
                        return ans
                    candidateDigit += 1

        factorFreqs = self._getFactorCount(primeFactors)
        onesLen = len(num) + 1 - sum(factorFreqs.values())
        return "1" * onesLen + "".join(d * factorFreqs[d] for d in sorted(factorFreqs.keys()))


    def _getPrimeCount(self, t: int) -> (Counter, bool):
        counts = Counter()
        for p in [2, 3, 5, 7]:
            while t % p == 0 and t > 0:
                counts[p] += 1
                t //= p
        return counts, t == 1

    def _getFactorCount(self, count: Counter) -> Counter:
        eights, remTwos = divmod(count[2], 3)
        nines, threes = divmod(count[3], 2)
        fours, twos = divmod(remTwos, 2)

        sixes = 0
        if twos == 1 and threes == 1:
            twos = 0
            threes = 0
            sixes = 1

        if threes == 1 and fours == 1:
            twos = 1
            sixes = 1
            threes = 0
            fours = 0

        return Counter({
            '2': twos,
            '3': threes,
            '4': fours,
            '5': count[5],
            '6': sixes,
            '7': count[7],
            '8': eights,
            '9': nines
        })

    # Helper to build a Counter from sum factor counts integer is not straightforward
    # Given prefixSum, which is sum of values of factor counts of digits processed
    # We cannot recover the prime factor counts directly.
    # Instead, adjust the final logic to properly compute needed factor counts by manual differences.

    # To fix the previous wrong approach with prefixSum subtraction, rewrite the digit processing block properly:


# Corrected version for the main function after reviewing the sums vs Counters:

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeFactors, divisibleFlag = self._getPrimeCount(t)
        if not divisibleFlag:
            return "-1"

        factorFreqs = self._getFactorCount(primeFactors)
        if sum(factorFreqs.values()) > len(num):
            resultStr = ""
            for digit in sorted(factorFreqs.keys()):
                resultStr += digit * factorFreqs[digit]
            return resultStr

        def get_factor_counts_digit(d: int) -> Counter:
            pf, div_flag = self._getPrimeCount(d)
            return self._getFactorCount(pf)

        prefixFactorCounts = Counter()
        for ch in num:
            d = int(ch)
            prefixFactorCounts += get_factor_counts_digit(d)

        zeroIdx = len(num)
        position = 0
        while position < len(num) and num[position] != "0":
            position += 1
        if position < len(num):
            zeroIdx = position

        # Check if prefixFactorCounts covers primeFactors (prefixFactorCounts >= primeFactors)
        is_prefix_sufficient = True
        for key, val in primeFactors.items():
            if prefixFactorCounts.get(key, 0) < val:
                is_prefix_sufficient = False
                break
        if zeroIdx == len(num) and is_prefix_sufficient:
            return num

        totalLen = len(num)
        for pos in range(totalLen - 1, -1, -1):
            currentDigit = int(num[pos])
            prefixFactorCounts -= get_factor_counts_digit(currentDigit)
            availableSpace = totalLen - 1 - pos
            if pos <= zeroIdx:
                candidateDigit = currentDigit + 1
                while candidateDigit <= 9:
                    candidateFactors = get_factor_counts_digit(candidateDigit)
                    neededFactors = primeFactors - (prefixFactorCounts + candidateFactors)
                    # Check if all neededFactors are non-negative
                    if all(v >= 0 for v in neededFactors.values()):
                        changeFactors = self._getFactorCount(neededFactors)
                        if sum(changeFactors.values()) <= availableSpace:
                            onesCount = availableSpace - sum(changeFactors.values())
                            prefix_part = num[:pos]
                            ans = prefix_part + str(candidateDigit) + "1" * onesCount
                            for d in sorted(changeFactors.keys()):
                                ans += d * changeFactors[d]
                            return ans
                    candidateDigit += 1

        factorFreqs = self._getFactorCount(primeFactors)
        onesLen = len(num) + 1 - sum(factorFreqs.values())
        return "1" * onesLen + "".join(d * factorFreqs[d] for d in sorted(factorFreqs.keys()))


    def _getPrimeCount(self, t: int) -> (Counter, bool):
        counts = Counter()
        for p in [2, 3, 5, 7]:
            while t % p == 0 and t > 0:
                counts[p] += 1
                t //= p
        return counts, t == 1

    def _getFactorCount(self, count: Counter) -> Counter:
        eights, remTwos = divmod(count[2], 3)
        nines, threes = divmod(count[3], 2)
        fours, twos = divmod(remTwos, 2)

        sixes = 0
        if twos == 1 and threes == 1:
            twos = 0
            threes = 0
            sixes = 1

        if threes == 1 and fours == 1:
            twos = 1
            sixes = 1
            threes = 0
            fours = 0

        return Counter({
            '2': twos,
            '3': threes,
            '4': fours,
            '5': count[5],
            '6': sixes,
            '7': count[7],
            '8': eights,
            '9': nines
        })