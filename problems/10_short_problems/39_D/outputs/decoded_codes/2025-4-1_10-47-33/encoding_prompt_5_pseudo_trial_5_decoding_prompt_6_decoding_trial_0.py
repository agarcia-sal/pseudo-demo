def main():
    # Get input from the user for both sets of numbers
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_set = first_input.split()
    second_set = second_input.split()

    # Initialize a counter for the number of differences
    difference_count = 0 

    # Loop through each position in the sets (there are 3 positions)
    for index in range(3):
        # Convert the current elements from strings to integers
        first_number = int(first_set[index])
        second_number = int(second_set[index])
        
        # Check if the numbers at the current position are different
        if first_number != second_number:
            # Increment difference count by 1
            difference_count += 1 

    # After checking all positions, decide the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Run the main function
main()
