from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        def countOccurrences(words):
            frequencyMap = defaultdict(int)

            def loopAllWords(idx):
                if idx == len(words):
                    return
                currentStr = words[idx]
                lenStr = len(currentStr)

                def loopStartPos(posStart):
                    if posStart == lenStr:
                        return

                    def loopEndPos(posEnd):
                        if posEnd > lenStr:
                            return
                        segment = currentStr[posStart:posEnd]
                        frequencyMap[segment] += 1
                        loopEndPos(posEnd + 1)

                    loopEndPos(posStart + 1)
                    loopStartPos(posStart + 1)

                loopStartPos(0)
                loopAllWords(idx + 1)

            loopAllWords(0)
            return frequencyMap

        counts = countOccurrences(arr)
        results = []

        def processString(idx):
            if idx == len(arr):
                return
            stringToCheck = arr[idx]
            strLen = len(stringToCheck)

            def findShortest(startPos, best):
                if startPos == strLen:
                    return best

                def checkEnd(endPos, candidate):
                    if endPos > strLen:
                        return candidate
                    part = stringToCheck[startPos:endPos]
                    if counts[part] == 1:
                        if len(candidate) == 0 or len(part) < len(candidate) or (len(part) == len(candidate) and part < candidate):
                            candidate = part
                    return checkEnd(endPos + 1, candidate)

                newBest = checkEnd(startPos + 1, best)
                return findShortest(startPos + 1, newBest)

            shortestCandidate = findShortest(0, "")
            results.append(shortestCandidate)
            processString(idx + 1)

        processString(0)
        return results