class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lengthVar = len(s)

        returnVal = 0

        pointerA = 0
        while pointerA <= lengthVar - 1:
            alpha = 0
            beta = 0
            pointerB = pointerA

            while pointerB <= lengthVar - 1:
                tempFlag = s[pointerB] == '1'
                if tempFlag:
                    alpha += 1
                else:
                    beta += 1

                if alpha >= beta * beta:
                    returnVal += 1

                pointerB += 1

            pointerA += 1

        return returnVal