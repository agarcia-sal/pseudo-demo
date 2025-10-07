class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        def toString(num):
            return str(num)

        def prefixSet(nums):
            tempSet = set()
            idx1 = 0
            while idx1 < len(nums):
                strNum = toString(nums[idx1])
                lenStr = len(strNum)

                def addPrefixes(s, n):
                    if n == 0:
                        return
                    tempSubstr = s[:n]
                    if tempSubstr not in tempSet:
                        tempSet.add(tempSubstr)
                    addPrefixes(s, n - 1)
                addPrefixes(strNum, lenStr)
                idx1 += 1
            return tempSet

        setA = prefixSet(arr1)
        setB = prefixSet(arr2)

        result = 0

        def maxInt(a, b):
            return a if a >= b else b

        keys = []
        for key in setA:
            keys.append(key)

        i = 0
        n = len(keys)

        def findLongest(lst):
            nonlocal i, n, result
            def innerLoop():
                nonlocal i, result
                if i >= n:
                    return
                ele = lst[i]
                if ele in setB:
                    result = maxInt(result, len(ele))
                i += 1
                innerLoop()
            innerLoop()

        findLongest(keys)

        return result