class Solution:
    def shortestSubstrings(self, arr):
        def incrementDict(dct, key):
            if key not in dct:
                dct[key] = 0
            dct[key] += 1

        def getLength(s):
            return len(s)

        def substrFromTo(text, startIdx, endIdxMinusOne):
            # Slice text from startIdx to endIdxMinusOne inclusive
            return text[startIdx:endIdxMinusOne+1]

        freqMap = {}
        idxArr = 0
        while idxArr < getLength(arr):
            currentStr = arr[idxArr]
            lenStr = getLength(currentStr)

            outerIdx = 0
            while outerIdx < lenStr:
                innerIdx = outerIdx + 1
                while True:
                    if innerIdx > lenStr:
                        break
                    subTxt = substrFromTo(currentStr, outerIdx, innerIdx - 1)
                    incrementDict(freqMap, subTxt)
                    innerIdx += 1
                outerIdx += 1
            idxArr += 1

        results = []
        posA = 0
        while posA < getLength(arr):
            element = arr[posA]
            elLen = getLength(element)
            custShortest = ""
            startI = 0
            while startI < elLen:
                endJ = startI + 1
                while endJ <= elLen:
                    candidate = substrFromTo(element, startI, endJ - 1)
                    if freqMap.get(candidate, 0) == 1:
                        if custShortest == "":
                            custShortest = candidate
                        else:
                            len_cand = getLength(candidate)
                            len_cust = getLength(custShortest)
                            if len_cand < len_cust:
                                custShortest = candidate
                            elif len_cand == len_cust:
                                # Lexicographically smaller check
                                lessString = False
                                x = 0
                                while x < len_cand and not lessString:
                                    if candidate[x] < custShortest[x]:
                                        lessString = True
                                    elif candidate[x] > custShortest[x]:
                                        lessString = False
                                        break
                                    x += 1
                                if lessString:
                                    custShortest = candidate
                    endJ += 1
                startI += 1
            results.append(custShortest)
            posA += 1

        return results