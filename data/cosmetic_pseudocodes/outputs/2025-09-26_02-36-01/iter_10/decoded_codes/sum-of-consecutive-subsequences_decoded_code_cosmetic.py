class Solution:
    def getSum(self, nums):
        def calc(inputArr):
            def createZeroList(length):
                # Recursively fill resultArr with zeros
                resultArr = [0] * length
                def rec_fillZeros(idx):
                    if idx == length:
                        return
                    resultArr[idx] = 0
                    rec_fillZeros(idx + 1)
                rec_fillZeros(0)
                return resultArr

            def newCounter():
                counts = {}
                return {
                    "incr": lambda k: counts.__setitem__(k, counts.get(k, 0) + 1),
                    "get": lambda k: counts.get(k, 0)
                }

            limit = len(inputArr)
            zeroArrLeft = createZeroList(limit)
            zeroArrRight = createZeroList(limit)
            freqCounter = newCounter()

            idx = 1
            while idx < limit:
                prevElem = inputArr[idx - 1]
                previouslySeen = freqCounter["get"](prevElem)
                toAdd = 1 + previouslySeen
                freqCounter["incr"](prevElem)
                zeroArrLeft[idx] = toAdd
                idx += 1

            freqCounter = newCounter()
            idxR = limit - 2
            while idxR >= 0:
                nextElem = inputArr[idxR + 1]
                ancestorCount = freqCounter["get"](nextElem)
                stepVal = ancestorCount + 1
                freqCounter["incr"](nextElem)
                zeroArrRight[idxR] = stepVal
                idxR -= 1

            def combineSum(arrA, arrB, arrC):
                resSum = 0
                pos = 0
                length = len(arrA)
                while pos < length:
                    A = arrA[pos]
                    B = arrB[pos]
                    C = arrC[pos]
                    part1 = A + B
                    part2 = A * B
                    coef = (part1 + part2) * C
                    resSum += coef
                    pos += 1
                return resSum

            return combineSum(zeroArrLeft, zeroArrRight, inputArr)

        constMod = 10**9 + 7
        leftResult = calc(nums)

        def reverseInPlace(arr):
            def swap(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            lo = 0
            hi = len(arr) - 1
            while lo < hi:
                swap(lo, hi)
                lo += 1
                hi -= 1

        reverseInPlace(nums)
        rightResult = calc(nums)

        def arrSum(a):
            acc = 0
            i = 0
            while True:
                if i >= len(a):
                    break
                acc += a[i]
                i += 1
            return acc

        combinedTotal = leftResult + rightResult + arrSum(nums)
        return combinedTotal % constMod