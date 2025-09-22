def main():
    # Step 1: Get user input
    first_input = input()   # Read first line of input
    second_input = input()  # Read second line of input

    # Step 2: Split inputs into lists of strings
    first_list = first_input.split()   # Split first_input into a list of strings
    second_list = second_input.split()  # Split second_input into a list of strings

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # Loop for the first three elements
        first_value = int(first_list[index])   # Convert string to integer
        second_value = int(second_list[index])  # Convert string to integer
        
        if first_value != second_value:  # Check if values differ
            difference_count += 1  # Increase difference count if values differ

    # Step 5: Determine the result based on the number of differences
    if difference_count < 3:  # If there are less than 3 differences
        print("YES")   # Print YES
    else:
        print("NO")    # Print NO

# Step 6: Start the program execution
if __name__ == "__main__":  # Check if the script is being executed directly
    main()   # Execute the main function
