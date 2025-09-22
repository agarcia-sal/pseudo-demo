def main_function():
    # Prompt the user for input
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of substrings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Ensure both lists have the same length before comparison
    if len(first_list) != len(second_list):
        print("ERROR: Input lists must be of equal length.")
        return

    # Compare corresponding elements in the two lists
    for index in range(3):  # Assuming we want to compare the first three components
        try:
            # Convert to integer
            first_value = int(first_list[index])
            second_value = int(second_list[index])
        except (ValueError, IndexError):
            print("ERROR: Invalid input data or insufficient elements.")
            return
        
        # Check if the values differ and increment the counter
        if first_value != second_value:
            difference_count += 1 

    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Initiates the main_function when the script is executed
if __name__ == "__main__":
    main_function()
