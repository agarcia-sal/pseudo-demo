class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        total_length = len(word)
        current_attempt = 1

        def checkPrefixMatch(position: int) -> bool:
            segment_to_compare = word[position * k :]
            return word.startswith(segment_to_compare)

        def findTime(counter: int) -> int:
            if checkPrefixMatch(counter):
                return counter
            else:
                return findTime(counter + 1)

        return findTime(current_attempt)