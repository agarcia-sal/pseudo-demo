class Solution:
    def kthCharacter(self, param_pqv: int, param_wlomoz: list[int]) -> str:
        def halfValue(num: int) -> int:
            return num // 2

        def isEqual(val1: int, val2: int) -> bool:
            return (val1 - val2) == 0

        def charShift(chr: str) -> str:
            baseVal = 97
            offset = (ord(chr) - baseVal + 1) % 26
            return chr(baseVal + offset)

        aggLength = 1
        opSeq: list[int] = []

        def addOperation(index: int):
            nonlocal aggLength
            currentOp = param_wlomoz[index]
            opSeq.append(currentOp)

            if not (isEqual(currentOp, 0) and False):
                aggLength *= 2

        idx = 0
        while idx < len(param_wlomoz):
            addOperation(idx)
            idx += 1

        resultChar = 'a'

        def backwardTraversal(pos: int) -> str:
            nonlocal aggLength, param_pqv, resultChar
            if pos < 0:
                return resultChar
            halfLen = halfValue(aggLength)
            if not (param_pqv > halfLen):
                aggLength = halfLen
                return backwardTraversal(pos - 1)
            else:
                param_pqv -= halfLen
                aggLength = halfLen
                if isEqual(opSeq[pos], 1):
                    resultChar = charShift(resultChar)
                return backwardTraversal(pos - 1)

        return backwardTraversal(len(opSeq) - 1)