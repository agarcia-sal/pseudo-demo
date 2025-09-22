def main():
    # Step 1: Obtain inputs from the user
    first_input = input()  # Prompt user for the first string of values
    second_input = input()  # Prompt user for the second string of values
    
    # Step 2: Split the input strings into lists of individual string values
    first_values = first_input.split()  # Create list of values from first input
    second_values = second_input.split()  # Create list of values from second input
    
    # Step 3: Initialize a counter for differences
    difference_count = 0  # Initialize a counter to track differences
    
    # Step 4: Compare the values in the two lists
    for index in range(3):  # We compare three pairs of values
        value_a = int(first_values[index])  # Convert current first value to integer
        value_b = int(second_values[index])  # Convert current second value to integer
        
        # Step 5: Check if the two values are different
        if value_a != value_b:  # If values are not equal
            difference_count += 1  # Increment the difference counter

    # Step 6: Determine the result based on the count of differences
    if difference_count < 3:  # If less than three differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Start the program execution
if __name__ == "__main__":  # Check if this module is the main module
    main()  # Call the main function
