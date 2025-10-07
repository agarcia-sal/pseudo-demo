from typing import List

class Solution:
    def occurrencesOfElement(self, numbers: List[int], requests: List[int], target: int) -> List[int]:
        StoreOccurrences = []
        IndexTracker = 0

        def TraverseList(lst: List[int]) -> None:
            nonlocal IndexTracker
            if IndexTracker >= len(lst):
                return
            if IsEqual(GetElement(lst, IndexTracker), target):
                RecordOccurrence(GetElement(lst, IndexTracker), IndexTracker)
            IncrementIndex()
            TraverseList(lst)

        def RecordOccurrence(value: int, idx: int) -> None:
            AppendToList(StoreOccurrences, idx)

        def IncrementIndex() -> None:
            nonlocal IndexTracker
            IndexTracker += 1

        def GetElement(container: List[int], pos: int) -> int:
            return container[pos]

        def AppendToList(container: List[int], val: int) -> None:
            container.append(val)

        def IsEqual(a: int, b: int) -> bool:
            return a == b

        TraverseList(numbers)

        ResultAnswers = []
        CurrentQueryIndex = 0

        def ProcessQueries(lst: List[int]) -> None:
            nonlocal CurrentQueryIndex
            if CurrentQueryIndex >= len(lst):
                return
            CurrentRequest = GetElement(lst, CurrentQueryIndex)
            if LessEqual(CurrentRequest, len(StoreOccurrences)):
                AppendToList(ResultAnswers, GetElement(StoreOccurrences, CurrentRequest - 1))
            else:
                AppendToList(ResultAnswers, ComputeMinusOne())
            IncrementQuery()
            ProcessQueries(lst)

        def LessEqual(a: int, b: int) -> bool:
            return a <= b

        def ComputeMinusOne() -> int:
            return -1

        def IncrementQuery() -> None:
            nonlocal CurrentQueryIndex
            CurrentQueryIndex += 1

        ProcessQueries(requests)
        return ResultAnswers