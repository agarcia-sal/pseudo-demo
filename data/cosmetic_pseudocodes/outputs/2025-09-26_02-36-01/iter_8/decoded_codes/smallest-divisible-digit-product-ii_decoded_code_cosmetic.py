from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter({'2': 1}),
    3: Counter({'3': 1}),
    4: Counter({'2': 2}),
    5: Counter({'5': 1}),
    6: Counter({'2': 1, '3': 1}),
    7: Counter({'7': 1}),
    8: Counter({'2': 3}),
    9: Counter({'3': 2}),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        alphaDelta_gar = self._getPrimeCount(t)
        lambOmega_vex = alphaDelta_gar[0]
        phiBeta_orb = alphaDelta_gar[1]

        if not phiBeta_orb:
            return "-1"

        gammaTheta_sip = self._getFactorCount(lambOmega_vex)

        omegaSum_lambda = sum(gammaTheta_sip.values())
        if omegaSum_lambda > len(num):
            etaRho_yen = ""
            for key in sorted(gammaTheta_sip.keys()):
                etaRho_yen += key * gammaTheta_sip[key]
            return etaRho_yen

        def accumulateFactorCount(str_input):
            betaSigma_rim = Counter()
            for char in str_input:
                intVal = int(char)
                countVals = FACTOR_COUNTS[intVal]
                for k in countVals:
                    betaSigma_rim[k] += countVals[k]
            return betaSigma_rim

        primeCountPrefix_psi = accumulateFactorCount(num)

        def findFirstZero(s):
            for idx_mu, ch in enumerate(s):
                if ch == "0":
                    return idx_mu
            return len(s)

        firstZeroIndex_zet = findFirstZero(num)

        # Check if all digits are nonzero and lambOmega_vex <= primeCountPrefix_psi by dict <= check
        # For Counter, can use (Counter1 & Counter2) == Counter1 iff all required keys counts are met
        # But here simplest is to check all keys in lambOmega_vex are less or equal counts in primeCountPrefix_psi
        if firstZeroIndex_zet == len(num):
            # Check if lambOmega_vex counts <= primeCountPrefix_psi counts for all keys
            if all(primeCountPrefix_psi.get(k, 0) >= v for k, v in lambOmega_vex.items()):
                return num

        def strRepeat(char_in, times_in):
            # Pythonic repeat
            return char_in * times_in

        lenNum_psi = len(num)
        zeroChar_const = "0"
        oneChar_const = "1"

        for revIndex in range(len(num) - 1, -1, -1):
            charCurrent = num[revIndex]
            digit_du = int(charCurrent)

            for key in primeCountPrefix_psi:
                primeCountPrefix_psi[key] -= FACTOR_COUNTS[digit_du].get(key, 0)
                if primeCountPrefix_psi[key] == 0:
                    del primeCountPrefix_psi[key]

            remainingSpace_mu = lenNum_psi - 1 - revIndex

            if revIndex <= firstZeroIndex_zet:
                higherDigit_delta = digit_du + 1
                while higherDigit_delta <= 9:
                    needed_prime = Counter(lambOmega_vex)  # copy to avoid mutation
                    for key in primeCountPrefix_psi:
                        needed_prime[key] -= primeCountPrefix_psi[key]
                    for key, val in FACTOR_COUNTS[higherDigit_delta].items():
                        needed_prime[key] -= val

                    # Remove zeros and negatives
                    keys_to_remove = [k for k, v in needed_prime.items() if v <= 0]
                    for k in keys_to_remove:
                        del needed_prime[k]

                    factorsAfterReplacement_li = self._getFactorCount(needed_prime)

                    sumFactorsAfter_sigma = sum(factorsAfterReplacement_li.values())

                    if sumFactorsAfter_sigma <= remainingSpace_mu:
                        fillOnesCount_nr = remainingSpace_mu - sumFactorsAfter_sigma

                        retval_psi = ""
                        if revIndex > 0:
                            retval_psi = num[:revIndex]
                        retval_psi += str(higherDigit_delta)
                        retval_psi += strRepeat(oneChar_const, fillOnesCount_nr)
                        for key in sorted(factorsAfterReplacement_li.keys()):
                            retval_psi += key * factorsAfterReplacement_li[key]

                        return retval_psi

                    higherDigit_delta += 1

        factorCountFinal_sig = self._getFactorCount(lambOmega_vex)
        sumFactorVal_psi = sum(factorCountFinal_sig.values())

        onesCount_wal = len(num) + 1 - sumFactorVal_psi

        ans_out = strRepeat(oneChar_const, onesCount_wal)
        for ky in sorted(factorCountFinal_sig.keys()):
            ans_out += ky * factorCountFinal_sig[ky]
        return ans_out

    def _getPrimeCount(self, t: int):
        countMap_lat = Counter()
        primes_arr = [2, 3, 5, 7]
        for pr in primes_arr:
            while t % pr == 0:
                t //= pr
                countMap_lat[pr] += 1
        return [countMap_lat, t == 1]

    def _getFactorCount(self, count):
        # count can be Counter with keys '2','3','4','5','6','7','8','9' or mapping int->count of primes 2,3,5,7
        # For _getFactorCount input: count is Counter with keys 2,3,5,7 and their multiplicities (integers)
        # But in accumulateFactorCount and _getPrimeCount, keys are int, so must be consistent

        # Ensure keys as integers 2,3,5,7 present:
        valTwo = count.get(2, 0) if isinstance(count, dict) else 0
        valThree = count.get(3, 0) if isinstance(count, dict) else 0
        valFive = count.get(5, 0) if isinstance(count, dict) else 0
        valSeven = count.get(7, 0) if isinstance(count, dict) else 0

        if isinstance(count, Counter) and all(isinstance(k, str) for k in count):
            # In case keys are string digits like '2','3', convert
            valTwo = count.get('2', 0)
            valThree = count.get('3', 0)
            valFive = count.get('5', 0)
            valSeven = count.get('7', 0)

        q8 = valTwo // 3
        rem2 = valTwo % 3

        q9 = valThree // 2
        rem3 = valThree % 2

        q4 = rem2 // 2
        rem4 = rem2 % 2

        cnt2 = rem4
        cnt3 = rem3
        cnt6 = 0

        if cnt2 == 1 and cnt3 == 1:
            cnt2 = 0
            cnt3 = 0
            cnt6 = 1

        if cnt3 == 1 and q4 == 1:
            cnt2 = 1
            cnt6 = 1
            cnt3 = 0
            q4 = 0

        resultCount_sko = Counter()
        resultCount_sko["2"] = cnt2
        resultCount_sko["3"] = cnt3
        resultCount_sko["4"] = q4
        resultCount_sko["5"] = valFive
        resultCount_sko["6"] = cnt6
        resultCount_sko["7"] = valSeven
        resultCount_sko["8"] = q8
        resultCount_sko["9"] = q9

        # Remove zero counts
        for k in list(resultCount_sko.keys()):
            if resultCount_sko[k] == 0:
                del resultCount_sko[k]

        return resultCount_sko