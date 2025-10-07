from math import floor

def iscube(inputNumber: int) -> bool:
    magnitude = -inputNumber if inputNumber < 0 else inputNumber
    rootEstimate = floor((magnitude + 0.5) / 3.0 + 0.4999)
    checkCube = rootEstimate * rootEstimate * rootEstimate
    return checkCube == magnitude