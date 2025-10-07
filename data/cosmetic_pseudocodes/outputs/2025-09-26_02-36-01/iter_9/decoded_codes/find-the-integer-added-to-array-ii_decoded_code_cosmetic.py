from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, walden1: List[int], walden2: List[int]) -> Optional[int]:
        def customSort(arts: List[int]) -> None:
            if not arts:
                return
            while True:
                swapped = False
                pvt = 0
                while pvt < len(arts) - 1:
                    if arts[pvt] > arts[pvt + 1]:
                        arts[pvt], arts[pvt + 1] = arts[pvt + 1], arts[pvt]
                        swapped = True
                    pvt += 1
                if not swapped:
                    break

        customSort(walden1)
        customSort(walden2)

        n = len(walden1)

        for subIndex1 in range(n - 1):
            for subIndex2 in range(subIndex1 + 1, n):
                filteredList = []
                # Append all elements except indices subIndex1 and subIndex2
                filteredList.extend(walden1[:subIndex1])
                filteredList.extend(walden1[subIndex1 + 1:subIndex2])
                filteredList.extend(walden1[subIndex2 + 1:])

                # filteredList should have length len(walden1)-2
                # walden2 length should match filteredList length to check mapping
                if not filteredList or len(filteredList) != len(walden2):
                    continue

                candidate = walden2[0] - filteredList[0]

                allMatch = True

                def checkMatch(counter=0):
                    nonlocal allMatch
                    if counter >= len(walden2):
                        return
                    if filteredList[counter] + candidate != walden2[counter]:
                        allMatch = False
                        return
                    checkMatch(counter + 1)

                checkMatch()

                if allMatch:
                    return candidate

        return None