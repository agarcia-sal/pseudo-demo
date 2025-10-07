from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        highest = 0

        def contains(setCollection: List[int], value: int) -> bool:
            for item in setCollection:
                if item == value:
                    return True
            return False

        def addElement(setCollection: List[int], value: int) -> None:
            setCollection.append(value)

        def removeElement(setCollection: List[int], value: int) -> None:
            tempList = []
            for element in setCollection:
                if element != value:
                    tempList.append(element)
            setCollection.clear()
            for element in tempList:
                setCollection.append(element)

        def sortDescending(arr: List[int]) -> None:
            if len(arr) <= 1:
                return
            for i in range(len(arr)):
                for j in range(len(arr) - i - 1):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        for i in range(len(grid)):
            sortDescending(grid[i])

        def explore(index: int, chosen: List[int], total: int) -> None:
            nonlocal highest
            if index >= len(grid):
                if total > highest:
                    highest = total
                return
            explore(index + 1, chosen, total)
            iterator = 0
            while iterator < len(grid[index]):
                element = grid[index][iterator]
                if not contains(chosen, element):
                    addElement(chosen, element)
                    explore(index + 1, chosen, total + element)
                    removeElement(chosen, element)
                iterator += 1

        explore(0, [], 0)
        return highest