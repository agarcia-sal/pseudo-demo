from typing import List

def decimal_to_binary(x: int) -> str:
    tempList: List[str] = ["db", ""]

    def build_binary(n: int) -> None:
        if n == 0:
            return
        build_binary(n // 2)
        tempList[1] += str(n % 2)

    if x == 0:
        tempList[1] = "0"
    else:
        build_binary(x)

    return tempList[0] + tempList[1] + tempList[0]