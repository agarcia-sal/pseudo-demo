class Solution:
    def numberOfSpecialChars(self, word):
        alphaFirst = {}
        alphaLast = {}
        cnt = 0

        def processIndex(idx, ch):
            if ch not in alphaFirst:
                alphaFirst[ch] = idx
            alphaLast[ch] = idx

        def enumerateChars(s, currentPos):
            if currentPos >= len(s):
                return
            processIndex(currentPos, s[currentPos])
            enumerateChars(s, currentPos + 1)

        enumerateChars(word, 0)

        lettersLower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        lettersUpper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        def runIterator(i):
            nonlocal cnt
            if i >= len(lettersLower):
                return

            lowerCh = lettersLower[i]
            upperCh = lettersUpper[i]

            if lowerCh in alphaLast and upperCh in alphaFirst:
                if alphaLast[lowerCh] < alphaFirst[upperCh]:
                    cnt += 1

            runIterator(i + 1)

        runIterator(0)

        return cnt