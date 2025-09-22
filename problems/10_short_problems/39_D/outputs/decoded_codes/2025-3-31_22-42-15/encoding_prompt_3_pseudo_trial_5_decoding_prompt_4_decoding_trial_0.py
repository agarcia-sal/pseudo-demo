def main():
    # Step 1: Gather input data
    first_input = input()  # Prompt user for first line of input
    second_input = input()  # Prompt user for second line of input
    
    # Step 2: Split the input strings into lists of strings
    first_list = first_input.split()  # Split first input by spaces
    second_list = second_input.split()  # Split second input by spaces
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Iterate through the first three elements of both lists
    for index in range(3):  # We are only interested in the first three elements
        # Convert the corresponding elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            difference_count += 1  # Increment the count of differences
    
    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO otherwise

# Execute the main function when the program starts
if __name__ == "__main__":
    main()
