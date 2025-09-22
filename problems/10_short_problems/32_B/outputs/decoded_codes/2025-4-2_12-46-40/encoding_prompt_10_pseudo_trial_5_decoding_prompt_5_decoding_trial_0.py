# Function to process the input string and create an output based on certain rules
def process_string():
    # Read input string from standard input
    input_string = input()
    # Remove whitespace from both ends of the input string
    input_string = input_string.strip()
    
    # Initialize index counter and answer string
    index = 0
    answer = ""
    
    # Loop through the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # Current character is a dot
            answer += '0'  # Append '0' to answer
            index += 1    # Increment index
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Next character is also a dot
            answer += '1'  # Append '1' to answer
            index += 2    # Increment index by 2
        else:
            # Neither of the above conditions are true
            answer += '2'  # Append '2' to answer
            index += 2    # Increment index by 2
    
    # Print the final answer string
    print(answer)

# Call the function to execute the processing
process_string()
