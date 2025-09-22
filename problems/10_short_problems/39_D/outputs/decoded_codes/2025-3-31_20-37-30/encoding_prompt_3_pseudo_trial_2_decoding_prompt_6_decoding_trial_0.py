def main():
    # Step 1: Get input values
    first_input = input()  # Accept first input from user
    second_input = input()  # Accept second input from user

    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()  # Split first input by spaces
    second_list = second_input.split()  # Split second input by spaces

    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter to track number of differences

    # Step 4: Compare the corresponding elements of the two lists
    for index in range(3):  # Iterate over the first three indices
        first_element = int(first_list[index])  # Convert to integer
        second_element = int(second_list[index])  # Convert to integer
        
        # If elements are different, increment the counter
        if first_element != second_element:
            difference_count += 1  # Increment difference count

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Print YES if less than 3 differences
    else:
        print("NO")  # Print NO if 3 or more differences

# Step 6: Execute the main function if the program is run as main
if __name__ == "__main__":
    main()
