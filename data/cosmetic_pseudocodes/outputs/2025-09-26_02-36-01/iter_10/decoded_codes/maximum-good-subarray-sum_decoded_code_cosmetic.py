class DictionaryNode:
    __slots__ = ('currentKey', 'currentValue', 'next')
    def __init__(self, currentKey, currentValue, next):
        self.currentKey = currentKey
        self.currentValue = currentValue
        self.next = next

class Solution:
    def maximumSubarraySum(self, nums, k):
        def dictContainsKey(d, c):
            def containsHelper(dic, key, acc):
                if acc is False:
                    if dic is None:
                        return False
                    if key == dic.currentKey:
                        return True
                    else:
                        return containsHelper(dic.next, key, False)
                else:
                    return acc
            return containsHelper(d, c, False)

        def getDictValue(d, key, default):
            def getHelper(dic, k, defaultVal):
                if dic is None:
                    return defaultVal
                elif dic.currentKey == k:
                    return dic.currentValue
                else:
                    return getHelper(dic.next, k, defaultVal)
            return getHelper(d, key, default)

        def setDictValue(d, key, val):
            def setHelper(dic, k, v):
                if dic is None:
                    return DictionaryNode(k, v, None)
                elif dic.currentKey == k:
                    return DictionaryNode(k, v, dic.next)
                else:
                    return DictionaryNode(dic.currentKey, dic.currentValue, setHelper(dic.next, k, v))
            return setHelper(d, key, val)

        def maxVal(a, b):
            return a if a > b else b

        def minVal(a, b):
            return a if a < b else b

        def tailRecursiveLoop(idx, currSum, maxSum, minPrefixSumList):
            if idx >= len(nums):
                if maxSum != (-1 * 10**18):
                    return maxSum
                else:
                    return 0
            else:
                elem = nums[idx]
                candidate1Key = elem - k
                candidate2Key = elem + k

                candidate1Exists = dictContainsKey(minPrefixSumList, candidate1Key)
                candidate2Exists = dictContainsKey(minPrefixSumList, candidate2Key)
                candidate = maxSum

                if candidate1Exists:
                    retrievedValue1 = getDictValue(minPrefixSumList, candidate1Key, 0)
                    candidate = maxVal(candidate, max(currSum - retrievedValue1 + elem, candidate))

                if candidate2Exists:
                    retrievedValue2 = getDictValue(minPrefixSumList, candidate2Key, 0)
                    candidate = maxVal(candidate, max(currSum - retrievedValue2 + elem, candidate))

                if dictContainsKey(minPrefixSumList, elem):
                    existingVal = getDictValue(minPrefixSumList, elem, 10**18)
                    newVal = minVal(existingVal, currSum)
                    updatedDict = setDictValue(minPrefixSumList, elem, newVal)
                    return tailRecursiveLoop(idx + 1, currSum + elem, candidate, updatedDict)
                else:
                    updatedDict = setDictValue(minPrefixSumList, elem, currSum)
                    return tailRecursiveLoop(idx + 1, currSum + elem, candidate, updatedDict)

        return tailRecursiveLoop(0, 0, -1 * 10**18, None)