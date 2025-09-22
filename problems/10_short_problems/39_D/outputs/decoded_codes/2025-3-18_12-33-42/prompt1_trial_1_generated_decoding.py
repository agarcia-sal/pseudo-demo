def main():
    # Read two lines of input
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of values
    first_values_list = first_input.split()
    second_values_list = second_input.split()
    
    # Initialize a counter to track differences
    difference_count = 0 
    
    # Loop through the first three items in both lists
    for index in range(3):
        # Convert the current values from both lists to integers
        first_value = int(first_values_list[index])
        second_value = int(second_values_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the counter of differences
            difference_count += 1
    
    # Evaluate the number of differences to provide output
    if difference_count < 3:
        print("YES")  # Indicating the inputs are similar enough
    else:
        print("NO")   # Indicating the inputs are too different

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
