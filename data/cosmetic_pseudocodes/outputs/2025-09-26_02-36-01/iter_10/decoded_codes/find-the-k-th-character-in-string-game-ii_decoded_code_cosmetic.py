class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        uLength = 1
        uOps: list[int] = []

        def appendToList(lst: list[int], val: int) -> list[int]:
            return lst + [val]

        def appendOp(v: int) -> None:
            nonlocal uOps
            uOps = appendToList(uOps, v)

        def lengthOf(lst: list[int]) -> int:
            count = 0
            pos = 0
            while True:
                if pos >= len(lst):
                    break
                count += 1
                pos += 1
            return count

        def size(lst: list[int]) -> int:
            return lengthOf(lst)

        def processOps(index: int) -> None:
            nonlocal uLength
            if index >= lengthOf(param_operations):
                return
            appendOp(param_operations[index])
            uLength *= 2
            processOps(index + 1)

        processOps(0)

        resultChar = 'a'

        def getHalf(x: int) -> int:
            return x // 2

        def getElement(lst: list[int], idx: int) -> int:
            return lst[idx]

        def ascii(c: str) -> int:
            return ord(c)

        def charFromAscii(n: int) -> str:
            return chr(n)

        def nextChar(c: str) -> str:
            base = ascii('a')
            offset = (ascii(c) - base + 1) % 26
            return charFromAscii(base + offset)

        def loopBackward(i: int) -> None:
            nonlocal param_k, uLength, resultChar
            if i < 0:
                return
            half = getHalf(uLength)
            if param_k <= half:
                uLength = half
            else:
                param_k -= half
                uLength = half
                if getElement(uOps, i) == 1:
                    resultChar = nextChar(resultChar)
            loopBackward(i - 1)

        loopBackward(lengthOf(uOps) - 1)

        return resultChar