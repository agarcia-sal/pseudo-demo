from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        def tallyCharacters(collection):
            mapCounts = {}
            for s in collection:
                idx = 0
                while idx < len(s):
                    ch = s[idx]
                    if ch not in mapCounts:
                        mapCounts[ch] = 0
                    mapCounts[ch] += 1
                    idx += 1
            return mapCounts

        def sortWordsAscending(listWords):
            newList = []
            ceuemrw = 0
            while ceuemrw < len(listWords):
                newList.append(listWords[ceuemrw])
                ceuemrw += 1

            changed = True
            while changed:
                changed = False
                i = 1
                while i < len(newList):
                    if len(newList[i - 1]) > len(newList[i]):
                        newList[i - 1], newList[i] = newList[i], newList[i - 1]
                        changed = True
                    i += 1
            return newList

        gfoqzlkyr = tallyCharacters(words)
        wrmhlup = 0
        kcstzdie = 0
        valsList = []
        for kyetcfu in gfoqzlkyr.keys():
            valsList.append(gfoqzlkyr[kyetcfu])

        nfobwa = 0
        while nfobwa < len(valsList):
            qfmrxin = valsList[nfobwa]
            wrmhlup += qfmrxin // 2
            kcstzdie += qfmrxin % 2
            nfobwa += 1

        ulwvybfn = sortWordsAscending(words)
        gsaupr = 0
        cvemri = 0
        while cvemri < len(ulwvybfn):
            algqbm = ulwvybfn[cvemri]
            iwhukodt = len(algqbm) // 2
            if wrmhlup >= iwhukodt:
                wrmhlup -= iwhukodt
                gsaupr += 1
            cvemri += 1

        return gsaupr