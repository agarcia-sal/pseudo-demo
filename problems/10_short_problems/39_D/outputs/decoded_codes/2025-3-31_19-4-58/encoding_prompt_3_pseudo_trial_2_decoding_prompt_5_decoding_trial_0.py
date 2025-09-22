def main():
    # Step 1: Obtain inputs from the user
    first_input = input()  # First string of values
    second_input = input()  # Second string of values

    # Step 2: Split the input strings into lists of individual string values
    first_values = first_input.split()  # List of values from the first input
    second_values = second_input.split()  # List of values from the second input
    
    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter for the number of differences
    
    # Step 4: Compare the values in the two lists
    for index in range(3):  # We want to compare three pairs of values
        value_a = int(first_values[index])  # Convert the current value from first list to integer
        value_b = int(second_values[index])  # Convert the current value from second list to integer
        
        # Step 5: Check if the two values are different
        if value_a != value_b:
            difference_count += 1  # Increment the difference count if values are not equal

    # Step 6: Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")  # Output NO if differences are 3 or more

# Step 7: Start the program execution
if __name__ == "__main__":
    main()
