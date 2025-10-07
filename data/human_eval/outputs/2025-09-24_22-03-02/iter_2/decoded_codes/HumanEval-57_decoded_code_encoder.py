def monotonic(inputList):
    if inputList == sorted(inputList) or inputList == sorted(inputList, reverse=True):
        return True
    return False