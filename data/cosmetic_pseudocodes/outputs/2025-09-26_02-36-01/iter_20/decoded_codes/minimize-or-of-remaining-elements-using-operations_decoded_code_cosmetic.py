class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            def bitwiseAnd(x, y):
                return x & y

            def isZero(val):
                return val == 0

            def isMinusOne(val):
                return val == -1

            def increment(val):
                return val + 1

            alpha = -1
            bravo = 0

            def processList(lst, idx, acc):
                nonlocal alpha, bravo
                if idx >= len(lst):
                    return acc
                delta = lst[idx]
                if isMinusOne(alpha):
                    alpha = delta
                else:
                    alpha = bitwiseAnd(alpha, delta)
                if isZero(bitwiseAnd(alpha, target_or)):
                    alpha = -1
                else:
                    bravo = increment(bravo)
                    if bravo > k:
                        return False
                return processList(lst, idx + 1, acc)

            echo = processList(nums, 0, True)
            return echo is not False

        def powTwo(exp):
            if exp == 0:
                return 1
            else:
                return 2 * powTwo(exp - 1)

        max_possible_value = powTwo(30) - 1
        result = max_possible_value
        MAX_INTEGER_CONSTANT = max_possible_value

        def loopBits(bit):
            nonlocal result
            if bit > 29:
                return
            bit_mask = powTwo(bit)
            if (result & bit_mask) == 0:
                loopBits(bit + 1)
                return

            def logicalNot(val):
                return 1 if val == 0 else 0

            def logicalNotBitmask(val):
                return MAX_INTEGER_CONSTANT - val

            inverted_mask = MAX_INTEGER_CONSTANT - bit_mask
            candidate = result & inverted_mask
            xor_val = (MAX_INTEGER_CONSTANT - result) ^ bit_mask
            if canAchieve(xor_val, k):
                result = candidate
            loopBits(bit + 1)

        loopBits(0)
        return result