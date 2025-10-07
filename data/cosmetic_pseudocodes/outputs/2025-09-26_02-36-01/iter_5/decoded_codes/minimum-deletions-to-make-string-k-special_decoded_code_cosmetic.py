class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def tallyCharacters(seq, pos, tally):
            if pos == len(seq):
                return tally
            ch = seq[pos]
            updatedCount = tally[ch] + 1 if ch in tally else 1
            newTally = tally.copy()
            newTally[ch] = updatedCount
            return tallyCharacters(seq, pos + 1, newTally)

        charCountsMap = tallyCharacters(word, 0, {})

        def extractValues(map_, keys, idx, vals):
            if idx == len(keys):
                return vals
            key = keys[idx]
            val = map_[key]
            return extractValues(map_, keys, idx + 1, vals + [val])

        keyList = list(charCountsMap.keys())
        freqListUnsorted = extractValues(charCountsMap, keyList, 0, [])

        def sortAscending(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]

            def partition(i, sm, gr):
                if i == len(arr):
                    return sm, gr
                if arr[i] < pivot:
                    return partition(i + 1, sm + [arr[i]], gr)
                else:
                    return partition(i + 1, sm, gr + [arr[i]])

            lesserList, greaterList = partition(1, [], [])
            return sortAscending(lesserList) + [pivot] + sortAscending(greaterList)

        freqList = sortAscending(freqListUnsorted)

        INF = 10 * 100 * 1000  # large enough positive number
        minimalRemoveCount = INF

        def sumDeletionsAfter(index, maxAllowed, freqs, pos, accum):
            if pos > len(freqs) - 1:
                return accum
            if pos > index:
                diff = freqs[pos] - maxAllowed
                if diff > 0:
                    return sumDeletionsAfter(index, maxAllowed, freqs, pos + 1, accum + diff)
                else:
                    return sumDeletionsAfter(index, maxAllowed, freqs, pos + 1, accum)
            else:
                return sumDeletionsAfter(index, maxAllowed, freqs, pos + 1, accum)

        def sumDeletionsBefore(index, freqs, pos, accum):
            if pos >= index:
                return accum
            return sumDeletionsBefore(index, freqs, pos + 1, accum + freqs[pos])

        def processIndex(i, limit, freqs, currentMin):
            if i > limit:
                return currentMin
            allowedMaxFreq = freqs[i] + k
            deletionsAfter = sumDeletionsAfter(i, allowedMaxFreq, freqs, 0, 0)
            deletionsBefore = sumDeletionsBefore(i, freqs, 0, 0)
            totalDel = deletionsAfter + deletionsBefore
            newMin = totalDel if totalDel < currentMin else currentMin
            return processIndex(i + 1, limit, freqs, newMin)

        maximalIndex = len(freqList) - 1
        answer = processIndex(0, maximalIndex, freqList, minimalRemoveCount)

        return answer