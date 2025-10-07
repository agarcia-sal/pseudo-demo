class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        def multiplyByTwo(x: int) -> int:
            return x + x

        def divideByTwo(x: int) -> int:
            return x // 2  # integer division

        def nextChar(c: str) -> str:
            if c == 'z' or c == 'Z':
                return 'a'
            else:
                return chr(ord(c) + 1)

        def buildOpsList(ops: list[int], source: list[int], idx: int) -> list[int]:
            if idx == len(source):
                return ops
            newOps = ops + [source[idx]]
            return buildOpsList(newOps, source, idx + 1)

        def updateLengthForOps(ops: list[int], length: int, idx: int, resRef: list[int]) -> None:
            if idx == len(ops):
                resRef[0] = length
                return
            newLen = multiplyByTwo(length)
            updateLengthForOps(ops, newLen, idx + 1, resRef)

        def kthCharRecursive(idx: int, k: int, length: int, ops: list[int], c: str) -> str:
            if idx < 0:
                return c
            half = divideByTwo(length)
            if k <= half:
                return kthCharRecursive(idx - 1, k, half, ops, c)
            else:
                newK = k - half
                newLen = half
                updatedC = nextChar(c) if ops[idx] == 1 else c
                return kthCharRecursive(idx - 1, newK, newLen, ops, updatedC)

        internalOps = buildOpsList([], param_operations, 0)

        totalLengthRef = [0]
        updateLengthForOps(internalOps, 1, 0, totalLengthRef)
        totalLength = totalLengthRef[0]

        initialChar = 'a'

        return kthCharRecursive(len(internalOps) - 1, param_k, totalLength, internalOps, initialChar)