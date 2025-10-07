class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        totalChars = len(word)
        elapsedTime = 1
        while True:
            reachedPos = elapsedTime * k
            remainingSubstring = word[reachedPos:]
            initialSegment = word[:totalChars - reachedPos]
            if reachedPos >= totalChars or remainingSubstring == initialSegment:
                return elapsedTime
            elapsedTime += 1