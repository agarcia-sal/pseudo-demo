def main():
    # Get input from the user
    print("Enter the first set of values:")
    first_input = input()
    print("Enter the second set of values:")
    second_input = input()
    
    # Split the input into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the values in both lists
    for index in range(3):  # Assuming both lists will have exactly three values
        # Convert the current values from string to integer
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1 
    
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    main()
