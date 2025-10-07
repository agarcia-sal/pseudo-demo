def decimal_to_binary(decimal_number: int) -> str:
    def aux(accumulator: str, input: int) -> str:
        if input == 0:
            return accumulator
        return aux(str(input % 2) + accumulator, input // 2)

    binaryString = "0" if decimal_number == 0 else aux("", decimal_number)
    return "db" + binaryString + "db"