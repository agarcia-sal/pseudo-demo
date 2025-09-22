def main():
    # Get the first set of numbers from the user
    first_input = input()
    
    # Get the second set of numbers from the user
    second_input = input()
    
    # Split the inputs into lists of strings
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the range of the first three values
    for index in range(3):
        # Convert the current string values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            # If they are different, increase the counter
            difference_count += 1 
    
    # Check the count of differences to decide the output
    if difference_count < 3:
        # Less than three differences means they are similar
        print("YES")
    else:
        # Three or more differences means they are not similar
        print("NO")

# Start the program
main()
