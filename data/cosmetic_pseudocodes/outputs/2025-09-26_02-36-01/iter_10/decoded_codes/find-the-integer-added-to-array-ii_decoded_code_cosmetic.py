from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def bubbleList(LIST: List[int]) -> None:
            flag = True
            while flag:
                flag = False
                idx = 1
                while idx < len(LIST):
                    if LIST[idx - 1] > LIST[idx]:
                        LIST[idx - 1], LIST[idx] = LIST[idx], LIST[idx - 1]
                        flag = True
                    idx += 1

        bubbleList(nums1)
        bubbleList(nums2)

        def matchCondition(ARR_A: List[int], ARR_B: List[int], DELTA: int) -> bool:
            def checkElements(POS: int) -> bool:
                if POS >= len(ARR_B):
                    return True
                elif ARR_A[POS] + DELTA != ARR_B[POS]:
                    return False
                else:
                    return checkElements(POS + 1)
            return checkElements(0)

        def formFilteredList(SRC: List[int], LEFT_IDX: int, RIGHT_IDX: int) -> List[int]:
            def gatherParts(POS: int, ACC: List[int]) -> List[int]:
                if POS >= len(SRC):
                    return ACC
                elif POS == LEFT_IDX or POS == RIGHT_IDX:
                    return gatherParts(POS + 1, ACC)
                else:
                    return gatherParts(POS + 1, ACC + [SRC[POS]])
            return gatherParts(0, [])

        outerPos = 0

        def outerLoop() -> Optional[int]:
            nonlocal outerPos
            if outerPos >= len(nums1):
                return None
            else:
                innerPos = outerPos + 1

                def innerLoop() -> Optional[int]:
                    nonlocal innerPos, outerPos
                    if innerPos >= len(nums1):
                        outerPos += 1
                        return outerLoop()
                    else:
                        filteredList = formFilteredList(nums1, outerPos, innerPos)
                        if not filteredList or not nums2:
                            # If filteredList or nums2 is empty, no valid candidate can be formed
                            innerPos += 1
                            return innerLoop()
                        candidateX = nums2[0] - filteredList[0]

                        if matchCondition(filteredList, nums2, candidateX):
                            return candidateX
                        else:
                            innerPos += 1
                            return innerLoop()

                return innerLoop()

        return outerLoop()