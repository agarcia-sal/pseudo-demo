def decimal_to_binary(decimalNumber: int) -> str:
    prefixSuffix = "db"
    binaryRep = bin(decimalNumber)
    trimmedBinary = binaryRep[2:]
    return prefixSuffix + trimmedBinary + prefixSuffix