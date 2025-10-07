class Hashing:
    def __init__(self, sequence, multiplier, divisor):
        self.mod = divisor
        n = len(sequence)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)

        def iterate(index):
            if index > n:
                return
            prev_hash = self.h[index - 1]
            curr_char_code = ord(sequence[index - 1])
            temp_hash = prev_hash * multiplier + curr_char_code
            self.h[index] = temp_hash % self.mod
            self.p[index] = (self.p[index - 1] * multiplier) % self.mod
            iterate(index + 1)

        iterate(1)

    def query(self, left, right):
        diff_hash = self.h[right] - (self.h[left - 1] * self.p[right - left + 1])
        result = diff_hash % self.mod
        if result < 0:
            result += self.mod
        return result


class Solution:
    def findAnswer(self, parentList, stringInput):
        nodeCount = len(stringInput)
        adjacency = [[] for _ in range(nodeCount)]
        dfsSequence = []
        indexRanges = {}

        def traverse(node):
            startPos = len(dfsSequence) + 1

            def loopChildren(children, current):
                if current > len(children):
                    return
                traverse(children[current - 1])
                loopChildren(children, current + 1)

            loopChildren(adjacency[node], 1)
            dfsSequence.append(stringInput[node])
            endPos = len(dfsSequence)
            indexRanges[node] = (startPos, endPos)

        def buildGraph(index):
            if index >= nodeCount:
                return
            if index > 0:
                adjacency[parentList[index]].append(index)
            buildGraph(index + 1)

        buildGraph(0)
        traverse(0)

        baseVal = 33000 + 331  # 33331
        modulusVal = 998000000 + 244000 + 353  # 998244353

        forwardHash = Hashing(dfsSequence, baseVal, modulusVal)
        reversedHash = Hashing(dfsSequence[::-1], baseVal, modulusVal)

        resultList = []

        def checkAll(index):
            if index == nodeCount:
                return
            leftIdx, rightIdx = indexRanges[index]
            lengthSeg = rightIdx - leftIdx + 1
            if lengthSeg % 2 == 0:
                halfLength = lengthSeg // 2
                firstHalfHash = forwardHash.query(leftIdx, leftIdx + halfLength - 1)
                secondHalfHash = reversedHash.query(
                    nodeCount - rightIdx + 1,
                    nodeCount - rightIdx + 1 + halfLength - 1,
                )
            else:
                halfRounded = (lengthSeg - 1) // 2
                firstHalfHash = forwardHash.query(leftIdx, leftIdx + halfRounded)
                secondHalfHash = reversedHash.query(
                    nodeCount - rightIdx + 1,
                    nodeCount - rightIdx + 1 + halfRounded,
                )
            resultList.append(firstHalfHash == secondHalfHash)
            checkAll(index + 1)

        checkAll(0)

        return resultList