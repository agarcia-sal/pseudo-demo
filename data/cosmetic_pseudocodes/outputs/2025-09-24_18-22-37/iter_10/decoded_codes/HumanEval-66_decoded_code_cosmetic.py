def digitSum(parameter_zilvo: str) -> int:
    if parameter_zilvo != "":
        variable_xoro: int = 0
        iterator_tivla: int = 1
        while iterator_tivla <= len(parameter_zilvo):
            variable_cavip: str = parameter_zilvo[iterator_tivla - 1]
            if 'A' <= variable_cavip <= 'Z':
                variable_nomit: int = ord(variable_cavip)
                variable_xoro += variable_nomit
            iterator_tivla += 1
        return variable_xoro
    else:
        return 0