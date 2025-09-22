# Define the main function to process the input string
def process_string():
    # Read input string from the user
    a = input().strip()  # Strip to remove any leading or trailing whitespace

    # Replace occurrences in the string for better readability
    a = a.replace('dot', '.')
    a = a.replace('at', '@')

    # Ensure the string starts with 'dot' if it begins with a dot
    if a.startswith('.'):
        a = 'dot' + a[1:]

    # Initialize variables
    count = 0
    result_list = []
    
    # Ensure the string starts with 'at' if it begins with an '@'
    if a.startswith('@'):
        a = 'at' + a[2:]

    # Iterate through each character in the modified string
    for char in a:
        if char == '@':
            if count > 0:
                # If the previous character was also an '@', add 'at'
                result_list.append('at')
                count = 1
            else:
                result_list.append('@')
                count = 1
        else:
            # Add the character to the result list
            result_list.append(char)
            count = 0  # Reset count for non-@ characters

    # Join the result list into a single string
    result = ''.join(result_list)

    # Replace trailing dot with 'dot'
    if result.endswith('.'):
        result = result[:-1] + 'dot'

    # Output the final modified string
    print(result)

# Call the main function to execute the program
process_string()
