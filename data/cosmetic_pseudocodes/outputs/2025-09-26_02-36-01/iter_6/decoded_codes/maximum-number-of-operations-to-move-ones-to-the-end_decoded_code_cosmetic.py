class Solution:
    def maxOperations(self, t: str) -> int:
        result = 0
        tally = 0
        position = 0

        def IsOne(x: str) -> bool:
            return x == '1'

        def Recurse():
            nonlocal position, result, tally
            if position >= len(t):
                return

            currentChar = t[position]
            if IsOne(currentChar):
                tally += 1
            else:
                if position != 0:
                    priorChar = t[position - 1]
                    if IsOne(priorChar):
                        result += tally

            position += 1
            Recurse()

        Recurse()
        return result