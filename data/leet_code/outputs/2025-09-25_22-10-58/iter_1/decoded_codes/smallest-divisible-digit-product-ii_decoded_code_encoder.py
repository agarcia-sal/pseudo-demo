from collections import Counter

class Solution:  
    def smallestNumber(self, num: str, t: int) -> str:  
        primeCount, isDivisible = self._getPrimeCount(t)  
        if not isDivisible:  
            return "-1"  

        factorCount = self._getFactorCount(primeCount)  
        if sum(factorCount.values()) > len(num):  
            # If too many factors, just concatenate them as string
            return ''.join(f * factorCount[f] for f in sorted(factorCount.keys()))  

        primeCountPrefix = Counter()  
        for ch in num:  
            primeCountPrefix += self._getFactorCount(Counter({int(ch): 1}))  
        firstZeroIndex = next((i for i, c in enumerate(num) if c == '0'), len(num))  
        if firstZeroIndex == len(num) and sum(primeCount.values()) <= sum(primeCountPrefix.values()):  
            return num  

        for i in reversed(range(len(num))):  
            d = int(num[i])  
            primeCountPrefix -= self._getFactorCount(Counter({d: 1}))  
            spaceAfterThisDigit = len(num) - 1 - i  
            if i <= firstZeroIndex:  
                for biggerDigit in range(d+1, 10):  
                    # factorCount after replacing digit at i with biggerDigit
                    factorsAfterReplacement = self._getFactorCount(primeCount - primeCountPrefix - self._getFactorCount(Counter({biggerDigit: 1})))  
                    if sum(factorsAfterReplacement.values()) <= spaceAfterThisDigit:  
                        fillOnes = spaceAfterThisDigit - sum(factorsAfterReplacement.values())  
                        prefix = num[:i]  
                        return prefix + str(biggerDigit) + ('1' * fillOnes) + ''.join(f * factorsAfterReplacement[f] for f in sorted(factorsAfterReplacement.keys()))  

        factorCount = self._getFactorCount(primeCount)  
        fillOnes = len(num) + 1 - sum(factorCount.values())  
        return ('1' * fillOnes) + ''.join(f * factorCount[f] for f in sorted(factorCount.keys()))  

    def _getPrimeCount(self, t: int) -> tuple[Counter, bool]:  
        count = Counter()  
        for prime in [2, 3, 5, 7]:  
            while t % prime == 0:  
                t //= prime  
                count[prime] += 1  
        return count, (t == 1)  

    def _getFactorCount(self, count: Counter) -> Counter:  
        count8, rem2 = divmod(count[2], 3)  
        count9, count3 = divmod(count[3], 2)  
        count4, count2 = divmod(rem2, 2)  

        count6 = 0  
        if count2 == 1 and count3 == 1:  
            count2 = 0  
            count3 = 0  
            count6 = 1  
        elif count3 == 1 and count4 == 1:  
            count2 = 1  
            count6 = 1  
            count3 = 0  
            count4 = 0  

        return Counter({  
            '2': count2,  
            '3': count3,  
            '4': count4,  
            '5': count[5],  
            '6': count6,  
            '7': count[7],  
            '8': count8,  
            '9': count9  
        })