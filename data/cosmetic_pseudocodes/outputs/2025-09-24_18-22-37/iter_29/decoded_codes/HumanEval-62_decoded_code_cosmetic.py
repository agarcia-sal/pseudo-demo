from typing import List

def derivative(arrayOfNums: List[float]) -> List[float]:
    indexVar: int = 1
    resultingArray: List[float] = []
    while indexVar < len(arrayOfNums):
        tempProduct: float = arrayOfNums[indexVar] * indexVar
        resultingArray.append(tempProduct)
        indexVar += 1
    return resultingArray