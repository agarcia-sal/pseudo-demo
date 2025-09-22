def translate_symbols():
    # Read input
    input_string = input().strip()
    
    # Initialize variables
    index = 0
    result = ""
    
    # Process the string
    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2
            
    # Output result
    print(result)

# Call the function to execute
translate_symbols()
