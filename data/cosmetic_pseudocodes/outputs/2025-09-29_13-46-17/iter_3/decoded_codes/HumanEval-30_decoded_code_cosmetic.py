from typing import List

def get_positive(listOfNumbers: List[float]) -> List[float]:
    positiveCollection: List[float] = []
    for number in listOfNumbers:
        if not (number <= 0):
            positiveCollection.append(number)
    return positiveCollection