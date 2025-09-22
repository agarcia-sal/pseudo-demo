def main():
    # Read two lines of input representing two sets of numbers
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()

    # Initialize a counter for differences
    difference_count = 0

    # Iterate through the numbers at each corresponding position
    for index in range(3):
        # Convert the string numbers to integers
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])
        
        # Check if the numbers at the same position are different
        if first_number != second_number:
            # Increment the difference count by 1
            difference_count += 1

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
