from typing import List


def tri(integer_n: int) -> List[float]:
    StartIndex: int = 0
    ResultList: List[float] = []

    while StartIndex <= integer_n:
        if StartIndex == 0:
            ResultList.append(1)
        elif StartIndex == 1:
            ResultList.append(3)
        else:
            CurrentPos = StartIndex
            if CurrentPos % 2 == 0:
                ValueToAdd = (CurrentPos / 2) + 1
                ResultList.append(ValueToAdd)
            else:
                LeftPrev = ResultList[CurrentPos - 1]
                RightPrev = ResultList[CurrentPos - 2]
                MidVal = (CurrentPos + 3) / 2
                SumVal = LeftPrev + RightPrev + MidVal
                ResultList.append(SumVal)
        StartIndex += 1

    return ResultList