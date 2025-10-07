import math

def iscube(numberInput: int) -> bool:
    magnitude = numberInput
    if magnitude < 0:
        magnitude = -magnitude

    candidateRoot = round(math.exp(math.log(magnitude) / 3)) if magnitude != 0 else 0
    candidateCubed = candidateRoot * candidateRoot * candidateRoot

    return candidateCubed == magnitude