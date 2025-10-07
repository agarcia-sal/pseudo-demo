class Solution:
    def maxDifference(self, s: list[str], k: int) -> int:
        result = -9999999999
        chars = ['zero', 'one', 'two', 'three', 'four']
        pairs = []
        for xChar in chars:
            for yChar in chars:
                if xChar != yChar:
                    pairs.append((xChar, yChar))

        for firstChar, secondChar in pairs:
            minimumDifferences = {}
            prefixListA = [0]
            prefixListB = [0]
            leftPointer = 0

            for charIndex in range(len(s)):
                currentChar = s[charIndex]

                newPrefixA = prefixListA[-1] + 1 if currentChar == firstChar else 0
                prefixListA.append(newPrefixA)

                newPrefixB = prefixListB[-1] + 1 if currentChar == secondChar else 0
                prefixListB.append(newPrefixB)

                while (charIndex + 1 - leftPointer) >= k and prefixListA[leftPointer] < prefixListA[-1] and prefixListB[leftPointer] < prefixListB[-1]:
                    modKeyA = prefixListA[leftPointer] % 2
                    modKeyB = prefixListB[leftPointer] % 2
                    keyTuple = (modKeyA, modKeyB)
                    diff = prefixListA[leftPointer] - prefixListB[leftPointer]
                    if keyTuple not in minimumDifferences or minimumDifferences[keyTuple] > diff:
                        minimumDifferences[keyTuple] = diff
                    leftPointer += 1

                parityA = 1 - (prefixListA[-1] % 2)
                parityB = prefixListB[-1] % 2
                targetKey = (parityA, parityB)

                curDiff = prefixListA[-1] - prefixListB[-1]
                if targetKey in minimumDifferences:
                    candidateValue = curDiff - minimumDifferences[targetKey]
                    if candidateValue > result:
                        result = candidateValue
                else:
                    if curDiff > result:
                        result = curDiff

        return result