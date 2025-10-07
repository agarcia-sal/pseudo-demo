class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        totalLength = len(word)
        currentCount = 1

        def doesStartWith(w: str, pref: str) -> bool:
            # Check if string w starts with prefix pref
            if len(pref) > len(w):
                return False
            for i in range(len(pref)):
                if w[i] != pref[i]:
                    return False
            return True

        def extractSuffix(w: str, startIndex: int) -> str:
            # Extract the substring of w starting from startIndex till end
            return w[startIndex:]

        def recursiveSearch(counter: int) -> int:
            suffix = extractSuffix(word, counter * k)
            if doesStartWith(word, suffix):
                return counter
            else:
                return recursiveSearch(counter + 1)

        return recursiveSearch(currentCount)