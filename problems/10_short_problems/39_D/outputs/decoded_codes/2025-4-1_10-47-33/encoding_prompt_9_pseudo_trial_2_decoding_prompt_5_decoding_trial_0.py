def main():
    # Read input values
    first_input = input()  # Get user input for the first set of integers
    second_input = input()  # Get user input for the second set of integers

    # Split the input strings into separate integer components
    first_list = list(map(int, first_input.split()))  # Convert first input string to a list of integers
    second_list = list(map(int, second_input.split()))  # Convert second input string to a list of integers

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the three integers
    for index in range(3):
        first_value = first_list[index]  # Get the value from the first list
        second_value = second_list[index]  # Get the value from the second list
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1  # Increment the difference count by 1

    # Determine if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
