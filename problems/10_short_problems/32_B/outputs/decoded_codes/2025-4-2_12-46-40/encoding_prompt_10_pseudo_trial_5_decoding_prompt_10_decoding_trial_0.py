def process_string():
    # Read input from user and remove whitespace from both ends
    input_string = input().strip()
    
    # Initialize index counter and answer string
    index = 0
    answer = ""
    
    # Loop until the index reaches the length of input string
    while index < len(input_string):
        if input_string[index] == '.':
            answer += '0'  # Append '0' to the answer string
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # Append '1' to the answer string
            index += 2  # Move to the character after next
        else:
            answer += '2'  # Append '2' to the answer string
            index += 2  # Move to the character after next
    
    # Output the final answer string
    print(answer)

# When running this script, it will invoke the process_string function
if __name__ == "__main__":
    process_string()
