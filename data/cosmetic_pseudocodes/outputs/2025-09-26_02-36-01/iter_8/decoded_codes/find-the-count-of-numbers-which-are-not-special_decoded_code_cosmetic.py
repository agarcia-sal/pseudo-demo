import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            pos = 5
            delta = 6
            while pos * pos <= num:
                if num % pos == 0 or num % (pos + 2) == 0:
                    return False
                pos += delta
            return True

        startPrimeVal = math.ceil(math.sqrt(l))
        endPrimeVal = math.floor(math.sqrt(r))
        countSpecial = 0
        iteratorNum = startPrimeVal

        while iteratorNum <= endPrimeVal:
            if is_prime(iteratorNum):
                countSpecial += 1
            iteratorNum += 1

        rangeCount = (r - l) + 1
        resultVal = rangeCount - countSpecial
        return resultVal