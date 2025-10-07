class Solution:
    def answerString(self, inputWord: str, companionCount: int) -> str:
        if companionCount == 1:
            return inputWord

        candidate = self._lastSubstring(inputWord)
        limit = len(inputWord) - companionCount + 1
        endpoint = len(candidate)

        if endpoint > limit:
            endpoint = limit

        return candidate[:endpoint]

    def _lastSubstring(self, text: str) -> str:
        startIndex = 0
        compareIndex = 1
        offset = 0
        n = len(text)
        while compareIndex + offset < n:
            if text[startIndex + offset] == text[compareIndex + offset]:
                offset += 1
            else:
                if text[startIndex + offset] > text[compareIndex + offset]:
                    compareIndex += offset + 1
                    offset = 0
                else:
                    newBase = startIndex + offset + 1
                    if compareIndex > newBase:
                        startIndex = compareIndex
                    else:
                        startIndex = newBase
                    compareIndex = startIndex + 1
                    offset = 0

        return text[startIndex:]