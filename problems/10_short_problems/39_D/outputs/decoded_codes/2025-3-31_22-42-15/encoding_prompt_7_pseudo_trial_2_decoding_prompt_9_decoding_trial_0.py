def compare_input_values():
    # Prompt the user to enter the first input string
    first_input = input()
    # Prompt the user to enter the second input string
    second_input = input()
    
    # Split the input strings into lists of strings
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for mismatches
    mismatch_count = 0
    
    # Loop through the first three elements (assuming both lists have at least 3 elements)
    for index in range(3):
        # Convert the values from string to integer
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Increment the mismatch count if the values do not match
        if first_value != second_value:
            mismatch_count += 1
            
    # Check the count of mismatches and print the appropriate response
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# If this script is run as the main program
if __name__ == "__main__":
    compare_input_values()
