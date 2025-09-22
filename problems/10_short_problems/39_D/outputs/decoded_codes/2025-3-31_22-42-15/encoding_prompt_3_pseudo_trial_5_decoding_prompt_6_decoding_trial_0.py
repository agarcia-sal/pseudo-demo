def main():
    # Step 1: Gather input data
    first_input = input()  # Prompt user for the first line of input
    second_input = input()  # Prompt user for the second line of input
    
    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()  # Split first input by spaces
    second_list = second_input.split()  # Split second input by spaces
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Iterate through the first three elements of both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the corresponding elements to integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check if the two values are different
        if first_value != second_value:  # Compare the two values
            difference_count += 1  # Increment difference count if different
    
    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:  # If difference count is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the main function when the program starts
if __name__ == "__main__":
    main()  # Call Main
