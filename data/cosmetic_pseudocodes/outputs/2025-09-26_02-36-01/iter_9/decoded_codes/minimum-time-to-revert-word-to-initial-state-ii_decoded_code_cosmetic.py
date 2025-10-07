class Solution:
    def minimumTimeToInitialState(self, omega: str, z: int) -> int:
        def extractor(source: str, start_pos: int) -> str:
            # start_pos is 1-based index according to pseudocode
            idx = start_pos - 1  # convert to 0-based
            result = ""
            while True:
                if idx >= len(source):
                    break
                result += source[idx]
                idx += 1
            return result

        def prefixChecker(mainStr: str, subStr: str) -> bool:
            i = 0
            isEqual = True
            while i < len(subStr) and isEqual:
                if mainStr[i] != subStr[i]:
                    isEqual = False
                i += 1
            return isEqual

        length_var = len(omega)
        counter = 1
        running = True

        while running:
            startIndex = counter * z
            segment = extractor(omega, startIndex)
            if prefixChecker(omega, segment):
                running = False
                return counter
            counter += 1