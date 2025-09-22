def compare_input_values():
    # Prompt user to enter first input string
    first_input = input()
    # Prompt user to enter second input string
    second_input = input()
    
    # Split first_input by spaces into a list called first_values
    first_values = first_input.split()
    # Split second_input by spaces into a list called second_values
    second_values = second_input.split()
    
    # Initialize a counter variable mismatch_count to 0
    mismatch_count = 0
    
    # For each index from 0 to 2 do
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        # Convert first_values[index] to an integer and store in first_value
        first_value = int(first_values[index])
        # Convert second_values[index] to an integer and store in second_value
        second_value = int(second_values[index])
        
        # If first_value is not equal to second_value then
        if first_value != second_value:
            # Increment mismatch_count by 1
            mismatch_count += 1
            
    # If mismatch_count is less than 3 then
    if mismatch_count < 3:
        # Print "YES"
        print("YES")
    else:
        # Print "NO"
        print("NO")

# If this script is run as the main program
if __name__ == "__main__":
    compare_input_values()
