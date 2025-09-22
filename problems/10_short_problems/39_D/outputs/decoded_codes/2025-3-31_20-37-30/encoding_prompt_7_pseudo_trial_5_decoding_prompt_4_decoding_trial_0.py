def main():
    # Read two lines of input representing two sets of three values
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three values to compare both sets
    for index in range(3):
        # Convert the values from string to integer for comparison
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the current values are different
        if first_value != second_value:
            # Increment the difference count if they are not the same
            difference_count += 1
    
    # Determine the output based on the number of differences found
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function only if the script is run as the main program
if __name__ == "__main__":
    main()
