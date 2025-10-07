class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        def tally(collection):
            frequencyMap = {}
            for elem in collection:
                frequencyMap[elem] = frequencyMap.get(elem, 0) + 1
            return frequencyMap

        hashmap = tally(nums2)

        def processPairs(arr, map_, key):
            mKeys = list(map_.keys())
            mValues = list(map_.values())

            def helperLoop(mKeys, mValues, pos, total):
                if pos >= len(mKeys):
                    return total
                divisorCandidate = mKeys[pos]
                freqValue = mValues[pos]
                if key % (divisorCandidate * k) == 0:
                    updatedTotal = total + freqValue
                else:
                    updatedTotal = total
                return helperLoop(mKeys, mValues, pos + 1, updatedTotal)

            return helperLoop(mKeys, mValues, 0, 0)

        def outerIndexLoop(array, map_, idx, result):
            if idx >= len(array):
                return result
            currentVal = array[idx]
            newResult = result + processPairs(array, map_, currentVal)
            return outerIndexLoop(array, map_, idx + 1, newResult)

        return outerIndexLoop(nums1, hashmap, 0, 0)