def decode_symbols(symbols: str) -> str:
    index = 0
    result = ""

    while index < len(symbols):
        current_symbol = symbols[index]

        if current_symbol == '.':
            result += '0'
            index += 1  # Move to the next symbol
        elif index + 1 < len(symbols) and symbols[index + 1] == '.':
            result += '1'
            index += 2  # Skip the next symbol as well
        elif index + 1 < len(symbols) and symbols[index + 1] == '-':
            result += '2'
            index += 2  # Skip the next symbol as well
        else:
            # If the pattern does not match, break the loop
            break

    return result

# Read input symbols
input_symbols = input()
output_digits = decode_symbols(input_symbols)
print(output_digits)
