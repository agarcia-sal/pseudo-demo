def digitSum(param1: str) -> int:
    if param1 == "":
        return 0
    varA: int = 0
    varB: int = 0
    while varB < len(param1):
        varC = param1[varB]
        if 'A' <= varC <= 'Z':
            varA += ord(varC)
        varB += 1
    return varA