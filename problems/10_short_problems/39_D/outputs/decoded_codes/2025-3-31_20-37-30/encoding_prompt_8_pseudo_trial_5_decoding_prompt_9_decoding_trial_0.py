def main():
    # Get inputs from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of strings
    first_set = first_input.split()
    second_set = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare each corresponding number in both sets
    for index in range(3):
        first_number = int(first_set[index])
        second_number = int(second_set[index])

        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1
            
    # Determine if the count of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
