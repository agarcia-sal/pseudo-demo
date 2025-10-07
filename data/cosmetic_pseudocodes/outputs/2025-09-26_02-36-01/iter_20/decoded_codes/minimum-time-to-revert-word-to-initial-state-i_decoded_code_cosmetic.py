class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        def customLength(s: str) -> int:
            counter = 0
            while True:
                if counter >= len(s):
                    break
                counter += 1
            return counter

        def excerptSubstring(s: str, startIndex: int, endIndex: int) -> str:
            collection = []
            pointer = startIndex
            while True:
                if pointer >= endIndex:
                    break
                collection.append(s[pointer])
                pointer += 1
            return "".join(collection)

        alpha = customLength(word)
        beta = 1

        while True:
            if not (beta * k < alpha):
                leftSegment = excerptSubstring(word, beta * k, alpha)
                rightSegment = excerptSubstring(word, 0, alpha - (beta * k))
                if leftSegment == rightSegment:
                    return beta
            beta += 1