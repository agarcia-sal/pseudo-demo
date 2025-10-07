from collections import defaultdict
from typing import List, Set

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        self.localSort(nums)
        totalPairs = 0
        frequencyMap = defaultdict(int)
        index = 0
        while index < len(nums):
            currentNum = nums[index]
            permutationsSet = self.setWithElement(currentNum)
            digitsList = self.toCharList(str(currentNum))
            lenDigits = len(digitsList)
            self.recurseSwap(0, lenDigits, digitsList, permutationsSet)
            totalPairs += self.sumValues(frequencyMap, permutationsSet)
            frequencyMap[currentNum] += 1
            index += 1
        return totalPairs

    def recurseSwap(self, position: int, limit: int, digitArray: List[str], results: Set[int]) -> None:
        if position >= limit:
            return
        j = limit - 1
        while j >= position:
            self.swap(digitArray, position, j)
            results.add(int(self.concatChars(digitArray)))
            if position + 1 < limit:
                self.recurseSwap(position + 1, limit, digitArray, results)
            self.swap(digitArray, position, j)
            j -= 1

    def localSort(self, array: List[int]) -> None:
        n = len(array)
        i = 0
        while i < len(array):
            swapped = False
            k = 0
            while k < n - 1:
                if array[k] > array[k + 1]:
                    self.swap(array, k, k + 1)
                    swapped = True
                k += 1
            n -= 1
            i += 1
            if not swapped:
                break

    def setWithElement(self, element: int) -> Set[int]:
        return {element}

    def toCharList(self, string: str) -> List[str]:
        return list(string)

    def toInt(self, string: str) -> int:
        result = 0
        for ch in string:
            result = result * 10 + (ord(ch) - ord('0'))
        return result

    def concatChars(self, charList: List[str]) -> str:
        return ''.join(charList)

    def sumValues(self, freqMap: defaultdict, keysSet: Set[int]) -> int:
        total = 0
        for key in keysSet:
            total += freqMap[key]
        return total

    def swap(self, array: List, a: int, b: int) -> None:
        array[a], array[b] = array[b], array[a]