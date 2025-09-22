def main():
    # Step 1: Gather input data
    first_input = input()  # Prompt user for the first line of input
    second_input = input()  # Prompt user for the second line of input
    
    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()  # Splitting by spaces
    second_list = second_input.split()  # Splitting by spaces
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Iterate through the first three elements of both lists
    for index in range(3):  # For indices 0, 1, 2
        # Convert the corresponding elements to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the two values are different
        if first_value != second_value:  # If values are not equal
            difference_count += 1  # Increment the difference count
            
    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Execute the main function when the program starts
if __name__ == "__main__":  # If the program is run directly
    main()  # Call main function
