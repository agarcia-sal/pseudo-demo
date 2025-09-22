def compare_input_values():
    # Prompt the user to enter the first input string
    first_input = input()
    # Prompt the user to enter the second input string
    second_input = input()
    
    # Split the input strings by spaces into lists
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for mismatches
    mismatch_count = 0
    
    # Compare values at each index from 0 to 2
    for index in range(3):
        # Convert the values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check for mismatches
        if first_value != second_value:
            # Increment the mismatch count if they are not equal
            mismatch_count += 1
            
    # Output YES if fewer than 3 mismatches, otherwise NO
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Check if this script is run as the main program
if __name__ == "__main__":
    compare_input_values()
