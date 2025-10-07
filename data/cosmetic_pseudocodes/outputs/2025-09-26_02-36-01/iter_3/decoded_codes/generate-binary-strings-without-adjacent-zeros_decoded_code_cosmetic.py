from typing import List

class Solution:
    def validStrings(self, length: int) -> List[str]:
        if length == 1:
            return ["0", "1"]

        resultCollection = []
        stack = ["0", "1"]
        while stack:
            currentSeq = stack.pop()
            if len(currentSeq) == length:
                resultCollection.append(currentSeq)
            else:
                tailChar = currentSeq[-1]
                if tailChar == "1":
                    stack.append(currentSeq + "0")
                    stack.append(currentSeq + "1")
                else:
                    stack.append(currentSeq + "1")
        return resultCollection