class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def tallyCharacters(text, tally):
            for ch in text:
                tally[ch] = tally.get(ch, 0) + 1

        def extractValues(mapObj, arrRef):
            arrRef.clear()
            for key in mapObj:
                arrRef.append(mapObj[key])

        def sortAscending(listRef):
            n = len(listRef)
            x = 0
            while x < n - 1:
                y = 0
                while y < n - x - 1:
                    if listRef[y] > listRef[y + 1]:
                        listRef[y], listRef[y + 1] = listRef[y + 1], listRef[y]
                    y += 1
                x += 1

        charCount = {}
        tallyCharacters(word, charCount)

        frequencies = []
        extractValues(charCount, frequencies)

        sortAscending(frequencies)

        minDelete = float('inf')

        for j in range(len(frequencies)):
            allowMax = frequencies[j] + k
            countDel = 0

            # sumDeletionAfter procedure
            p = j + 1
            while p < len(frequencies):
                if frequencies[p] > allowMax:
                    countDel += frequencies[p] - allowMax
                p += 1

            q = 0
            while q < j:
                countDel += frequencies[q]
                q += 1

            if countDel < minDelete:
                minDelete = countDel

        return minDelete