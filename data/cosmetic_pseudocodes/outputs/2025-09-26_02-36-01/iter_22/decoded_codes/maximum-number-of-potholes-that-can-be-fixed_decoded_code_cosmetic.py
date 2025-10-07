class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def splitAtFullStop(input_str: str) -> list[str]:
            results = []
            start = 0
            index = 0
            length = len(input_str)
            while index < length:
                if input_str[index] == '.':
                    results.append(input_str[start:index])
                    start = index + 1
                index += 1
            if start <= length:
                results.append(input_str[start:length])
            return results

        segments = splitAtFullStop(road)

        def ascendingLengthSort(arr: list[str]) -> list[str]:
            changed = True
            while changed:
                changed = False
                i = 0
                while i < len(arr) - 1:
                    if len(arr[i]) > len(arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        changed = True
                    i += 1
            return arr

        sortedSegments = ascendingLengthSort(segments)

        totalFixed = 0
        segmentIndex = 0

        while segmentIndex < len(sortedSegments):
            fragment = sortedSegments[segmentIndex]
            fragmentLength = len(fragment)

            if fragmentLength != 0:
                requiredCost = fragmentLength + 1

                if budget >= requiredCost:
                    totalFixed += fragmentLength
                    budget -= requiredCost
                else:
                    lengthTracker = fragmentLength
                    continueLoop = True

                    while continueLoop and lengthTracker > 0 and budget > 0:
                        requiredCost = lengthTracker + 1
                        if budget >= requiredCost:
                            totalFixed += lengthTracker
                            budget -= requiredCost
                            continueLoop = False
                        else:
                            lengthTracker -= 1

            segmentIndex += 1

        return totalFixed