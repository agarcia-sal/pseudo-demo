from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, alpha):
        modulus = 10**9 + 7
        counts = defaultdict(int)
        accumulators = defaultdict(int)

        def addMod(a, b):
            temp_sum = a + b
            if temp_sum >= modulus:
                return temp_sum - modulus
            else:
                return temp_sum

        def getMapSafe(m, k):
            return m[k] if k in m else 0

        length_alpha = len(alpha)

        def processElement(elem):
            counts[elem] = addMod(getMapSafe(counts, elem), 1)

            accumulators[elem] = addMod(getMapSafe(accumulators, elem), elem)

            part1 = getMapSafe(accumulators, elem)
            part2 = getMapSafe(accumulators, elem - 1)
            part3 = getMapSafe(counts, elem - 1) * elem
            new_accumulator = part1 + part2 + part3
            accumulators[elem] = new_accumulator % modulus

            counts[elem] = addMod(getMapSafe(counts, elem), getMapSafe(counts, elem - 1))

            part4 = getMapSafe(accumulators, elem)
            part5 = getMapSafe(accumulators, elem + 1)
            part6 = getMapSafe(counts, elem + 1) * elem
            new_accumulator2 = part4 + part5 + part6
            accumulators[elem] = new_accumulator2 % modulus

            counts[elem] = addMod(getMapSafe(counts, elem), getMapSafe(counts, elem + 1))

        def iterateElements(idx):
            if idx >= length_alpha:
                return
            processElement(alpha[idx])
            iterateElements(idx + 1)

        iterateElements(0)

        def accumulateTotal(m):
            sum_accumulator = 0
            keys = list(m.keys())
            idx = 0
            while idx < len(keys):
                sum_accumulator += m[keys[idx]]
                idx += 1
            return sum_accumulator

        overall_sum = accumulateTotal(accumulators)
        answer = overall_sum % modulus

        return answer