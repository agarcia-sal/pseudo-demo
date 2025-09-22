# Main process to compare two sets of values
def main():
    # Get the first set of values from the user
    first_input = input()
    # Get the second set of values from the user
    second_input = input()
    
    # Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Initialize a counter for the differences
    difference_count = 0
    
    # Loop through indices from 0 to 2 (inclusive)
    for index in range(3):
        # Convert the current index values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1

    # Check if fewer than three differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
