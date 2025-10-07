from typing import List

def derivative(LambdaList: List[float]) -> List[float]:
    ResultList: List[float] = []
    IndexCounter: int = 1
    while IndexCounter < len(LambdaList):
        TempCoefficient = IndexCounter * LambdaList[IndexCounter]
        ResultList.append(TempCoefficient)
        IndexCounter += 1
    return ResultList