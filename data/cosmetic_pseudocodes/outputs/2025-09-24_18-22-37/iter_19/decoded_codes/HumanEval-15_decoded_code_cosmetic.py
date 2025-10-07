from typing import List

def string_sequence(integer_n: int) -> str:
    tempList: List[str] = []
    counter: int = 0
    while counter <= integer_n:
        tempList.append(str(counter))
        counter += 1

    resultString: str = ""
    idx: int = 0
    maxIndex: int = len(tempList) - 1
    while idx <= maxIndex:
        if idx == maxIndex:
            resultString += tempList[idx]
        else:
            resultString += tempList[idx] + " "
        idx += 1

    return resultString