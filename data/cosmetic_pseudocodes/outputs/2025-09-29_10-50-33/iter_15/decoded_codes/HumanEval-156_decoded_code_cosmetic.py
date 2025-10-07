from typing import List


def int_to_mini_roman(value: int) -> str:
    valuesList: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbolsList: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    indexCounter: int = 0
    finalOutput: str = ""

    while True:
        if value > 0:
            times: int = 0
            while value >= valuesList[indexCounter]:
                value -= valuesList[indexCounter]
                times += 1

            symbolAdder: int = 0
            while symbolAdder < times:
                finalOutput += symbolsList[indexCounter]
                symbolAdder += 1

            indexCounter += 1
        else:
            break

    return finalOutput.lower()