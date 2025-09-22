def convert_string_to_numbers():
    # Read a line of input and strip any leading/trailing whitespace
    input_string = input().strip()
    
    # Initialize an index to traverse the string and a variable to store the result
    index = 0
    result = ""

    # Loop through the string until the end is reached
    while index < len(input_string):
        # Check if the current character is a period (.)
        if input_string[index] == '.':
            # Append '0' to the result for a single period
            result += '0'
            # Move to the next character
            index += 1
        else:
            # Check if the next character is also a period (.)
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                # Append '1' to the result for a pair of periods
                result += '1'
                # Move the index forward by 2 characters
                index += 2
            else:
                # Append '2' to the result for any other characters
                result += '2'
                # Move the index forward by 2 characters
                index += 2
            
    # Output the final result
    print(result)

# To call the function and execute it, uncomment the line below:
# convert_string_to_numbers()
