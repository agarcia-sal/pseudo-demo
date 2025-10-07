def digits(paramA: int) -> int:
    temp1: int = 1
    temp2: int = 0
    iteratorX: int = 0
    param_str: str = str(paramA)

    while iteratorX < len(param_str):
        temp3: int = int(param_str[iteratorX])
        if temp3 % 2 == 1:
            temp1 *= temp3
            temp2 += 1
        iteratorX += 1

    return 0 if temp2 == 0 else temp1