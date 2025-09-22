# Function to convert a string of symbols into corresponding digits
def convert_symbols_to_digits():
    input_string = input()
    index = 0
    result = ""

    while index < len(input_string):
        if input_string[index] == ".":
            result += "0"  # single dot
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == ".":
            result += "1"  # double dots
            index += 2
        elif index + 1 < len(input_string) and input_string[index] == "-" and input_string[index + 1] == ".":
            result += "2"  # dash followed by dot
            index += 2
        else:
            # Handle unexpected characters if necessary
            index += 1  # Just move forward to avoid infinite loop in unexpected cases

    print(result)

# Call the function to execute the conversion
convert_symbols_to_digits()
