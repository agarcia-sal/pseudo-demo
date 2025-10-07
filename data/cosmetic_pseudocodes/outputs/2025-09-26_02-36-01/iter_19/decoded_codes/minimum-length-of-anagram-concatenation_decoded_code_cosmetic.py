class Solution:
    def minAnagramLength(self, k: str) -> int:
        countSet = self.CreateEmptySet()
        index = 0
        while index < self.LengthOf(k):
            self.InsertIntoSet(countSet, self.GetCharAt(k, index))
            index += 1
        return self.GetSetSize(countSet)

    def CreateEmptySet(self) -> set:
        return set()

    def InsertIntoSet(self, ctSet: set, val: str) -> None:
        ctSet.add(val)

    def GetCharAt(self, s: str, pos: int) -> str:
        return s[pos]

    def LengthOf(self, x: str) -> int:
        return len(x)

    def GetSetSize(self, xSet: set) -> int:
        return len(xSet)