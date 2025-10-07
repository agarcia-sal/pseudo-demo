class Solution:
    def minimumLength(self, s):
        def modTwo(n):
            return n - ((n // 2) * 2)

        def incrementByOne(val):
            return val + 1

        def incrementByTwo(val):
            return val + 2

        def isZero(n):
            return n == 0

        def notEquals(a, b):
            return not (a == b)

        def getValues(d):
            def collectKeys(keysList, resultList, index):
                if index >= len(keysList):
                    return resultList
                else:
                    resultList.append(d[keysList[index]])
                    return collectKeys(keysList, resultList, index + 1)
            return collectKeys(list(d.keys()), [], 0)

        def countElements(arr):
            def countHelper(accumMap, idx):
                if idx >= len(arr):
                    return accumMap
                else:
                    key = arr[idx]
                    if key not in accumMap:
                        accumMap[key] = 1
                    else:
                        accumMap[key] += 1
                    return countHelper(accumMap, idx + 1)
            return countHelper({}, 0)

        frequencyMap = countElements(s)
        valuesList = getValues(frequencyMap)

        def processCountList(lst):
            def loop(index, oddSum, evenSum):
                if index >= len(lst):
                    return [oddSum, evenSum]
                else:
                    val = lst[index]
                    rem = modTwo(val)
                    if rem == 1:
                        return loop(index + 1, incrementByOne(oddSum), evenSum)
                    elif rem == 0 and notEquals(val, 0):
                        return loop(index + 1, oddSum, incrementByTwo(evenSum))
                    else:
                        return loop(index + 1, oddSum, evenSum)
            return loop(0, 0, 0)

        sums = processCountList(valuesList)
        finalResult = sums[0] + sums[1]

        return finalResult