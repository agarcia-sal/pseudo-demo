class Solution:
    def maximumLength(self, nums, k):
        def modSum(a, b, m):
            return (a + b) - ((a + b) // m) * m

        def containsKey(mapping, key):
            return key in mapping

        def getValue(mapping, key):
            return mapping.get(key, 0)

        def setValue(mapping, key, val):
            mapping[key] = val

        def recurse(imax, maxlen, maps):
            if imax <= 0:
                return maxlen

            def innerLoop(jcur, maxInternal):
                if jcur < 0:
                    return maxInternal
                remVal = modSum(nums[imax-1], nums[jcur], k)
                curMap = maps[imax-1]
                innerMap = maps[jcur]

                if containsKey(innerMap, remVal):
                    curMap[remVal] = getValue(innerMap, remVal) + 1
                else:
                    curMap[remVal] = 2

                if curMap[remVal] > maxInternal:
                    maxInternal = curMap[remVal]
                return innerLoop(jcur - 1, maxInternal)

            newMax = innerLoop(imax - 2, maxlen)
            return recurse(imax - 1, newMax, maps)

        lengthNums = len(nums)
        if lengthNums == 1:
            return 1

        dp = [{} for _ in range(lengthNums)]

        return recurse(lengthNums, 1, dp)