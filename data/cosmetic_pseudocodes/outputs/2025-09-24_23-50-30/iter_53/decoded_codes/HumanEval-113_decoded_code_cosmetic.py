from typing import List, Union

def odd_count(parameterA: List[List[Union[int, str]]]) -> List[str]:
    variableX: List[str] = []

    def innerFunc(indexA: int) -> None:
        if indexA < len(parameterA):
            variableY = 0
            for elementB in parameterA[indexA]:
                if int(elementB) % 2 == 1:
                    variableY += 1
            variableX.append(
                "the number of odd elements "
                + str(variableY)
                + "n the str"
                + str(variableY)
                + "ng "
                + str(variableY)
                + " of the "
                + str(variableY)
                + "nput."
            )
            innerFunc(indexA + 1)

    innerFunc(0)
    return variableX