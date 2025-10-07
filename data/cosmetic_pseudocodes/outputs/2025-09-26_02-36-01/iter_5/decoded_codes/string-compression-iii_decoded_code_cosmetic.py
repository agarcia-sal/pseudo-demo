class Solution:
    def compressedString(self, word: str) -> str:
        def recurEncode(position: int, acc: str) -> str:
            if position >= len(word):
                return acc
            currentChar = word[position]

            def countRepeats(idx: int, charNow: str, num: int) -> int:
                if idx >= len(word) or word[idx] != charNow or num == 9:
                    return num
                return countRepeats(idx + 1, charNow, num + 1)

            tally = countRepeats(position, currentChar, 0)
            appendedSegment = str(tally) + currentChar
            return recurEncode(position + tally, acc + appendedSegment)

        return recurEncode(0, "")