def digitSum(input_value: str) -> int:
    if input_value == "":
        return 0
    accumulator = 0
    for element in input_value:
        if "A" <= element <= "Z":
            accumulator += ord(element)
        else:
            accumulator += 0
    return accumulator