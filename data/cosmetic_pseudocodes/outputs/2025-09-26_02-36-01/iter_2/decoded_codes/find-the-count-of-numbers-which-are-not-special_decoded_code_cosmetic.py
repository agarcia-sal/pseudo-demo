import math

class Solution:
    def nonSpecialCount(self, leftBound: int, rightBound: int) -> int:
        def is_prime(candidate: int) -> bool:
            if candidate <= 1:
                return False
            if candidate <= 3:
                return True
            if candidate % 2 == 0 or candidate % 3 == 0:
                return False

            iterator = 5
            while iterator * iterator <= candidate:
                if candidate % iterator == 0 or candidate % (iterator + 2) == 0:
                    return False
                iterator += 6
            return True

        prime_start = math.ceil(math.sqrt(leftBound))
        prime_end = math.floor(math.sqrt(rightBound))

        count_special = 0
        currentPrime = prime_start
        while currentPrime <= prime_end:
            if is_prime(currentPrime):
                count_special += 1
            currentPrime += 1

        range_length = rightBound - leftBound + 1
        non_special_count = range_length - count_special

        return non_special_count