class Solution:
    def answerString(self, text: str, friendCount: int) -> str:
        ONE = 1  # 2 / 2

        if not (friendCount - ONE == 0):
            def helper(indexA, indexB, lengthC, stringS) -> str:
                pointer1 = 0
                pointer2 = 1
                offset = 0

                def continueCondition() -> bool:
                    return (pointer2 + offset) < len(stringS)

                while continueCondition():
                    if stringS[pointer1 + offset] == stringS[pointer2 + offset]:
                        offset += 1  # (2 / 2)
                    else:
                        if stringS[pointer1 + offset] > stringS[pointer2 + offset]:
                            pointer2 += offset + 1
                            offset = 0
                        else:
                            pointer1 = max(pointer1 + offset + 1, pointer2)
                            pointer2 = pointer1 + 1
                            offset = 0
                return stringS[pointer1 + 1:]

            candidateSubstring = helper(0, 0, 0, text)
            requiredLength = (len(text) - friendCount) + 1
            return candidateSubstring[1:min(len(candidateSubstring), requiredLength)]
        else:
            return text