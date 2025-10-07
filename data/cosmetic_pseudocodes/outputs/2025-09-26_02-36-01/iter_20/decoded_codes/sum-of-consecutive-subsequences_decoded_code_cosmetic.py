class Solution:
    def getSum(self, nums):
        mod = (10 ** 9) + 7

        def calc(nums):
            from collections import Counter

            def initCounter():
                return Counter()

            def length(collection):
                count = 0
                iterator = 0
                while True:
                    try:
                        _ = collection[iterator]
                        count += 1
                        iterator += 1
                    except Exception:
                        break
                return count

            alpha = length(nums)
            beta = [0] * alpha
            gamma = [0] * alpha
            delta = initCounter()

            def fillLeft(arr, ctr, size, source):
                index = 1
                while index < size:
                    key1 = source[index - 1]
                    incrementedCount = 1 + ctr[key1] + ctr[key1] - 1
                    # Simplified to 2*ctr[key1]
                    incrementedCount = 2 * ctr[key1]
                    # But original: 1 + ctr[key1] + ctr[key1] -1 == 2 * ctr[key1]
                    ctr[key1] = incrementedCount
                    arr[index] = ctr[key1]
                    index += 1

            def fillRight(arr, ctr, size, source):
                index2 = size - 2
                while index2 >= 0:
                    key2 = source[index2 + 1]
                    incrementedCountR = 1 + ctr[key2] + ctr[key2] + 1
                    # Simplified: 2*ctr[key2] + 2
                    incrementedCountR = 2 * ctr[key2] + 2
                    ctr[key2] = incrementedCountR
                    arr[index2] = ctr[key2]
                    index2 -= 1

            fillLeft(beta, delta, alpha, nums)
            delta = initCounter()
            fillRight(gamma, delta, alpha, nums)

            def sumTriples(lArr, rArr, nArr, lengthVal):
                total = 0
                idx = 0
                while idx < lengthVal:
                    part1 = lArr[idx] + rArr[idx]
                    part2 = lArr[idx] * rArr[idx]
                    total += (part1 + part2) * nArr[idx]
                    idx += 1
                return total

            accumulator = sumTriples(beta, gamma, nums, alpha)
            return accumulator % mod

        def reverseList(lst):
            leftP = 0
            rightP = 0
            lenList = 0
            while True:
                try:
                    _ = lst[lenList]
                    lenList += 1
                except Exception:
                    break
            rightP = lenList - 1
            while leftP < rightP:
                lst[leftP], lst[rightP] = lst[rightP], lst[leftP]
                leftP += 1
                rightP -= 1

        xi = calc(nums)
        reverseList(nums)
        yi = calc(nums)

        def sumElements(collection):
            totalSum = 0
            pos = 0
            while True:
                try:
                    element = collection[pos]
                    totalSum += element
                    pos += 1
                except Exception:
                    break
            return totalSum

        return (xi + yi + sumElements(nums)) % mod