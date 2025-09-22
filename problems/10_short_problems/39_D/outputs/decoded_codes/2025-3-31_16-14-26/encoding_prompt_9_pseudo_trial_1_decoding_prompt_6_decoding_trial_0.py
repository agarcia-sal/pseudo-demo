# Define the main function to execute the program
def main():
    # Receive Input: Prompt the user to enter two sets of three integers as strings
    first_input = input()
    second_input = input()

    # Split the input strings into lists of integers
    first_set = list(map(int, first_input.split()))
    second_set = list(map(int, second_input.split()))

    # Initialize the difference counter
    difference_count = 0

    # Compare corresponding items in the two sets
    for index in range(3):  # Loop through indices 0 to 2
        first_number = first_set[index]
        second_number = second_set[index]

        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1  # Increment the counter for each difference

    # Determine result based on the count of differences
    if difference_count < 3:
        print("YES")  # Print YES if differences are fewer than 3
    else:
        print("NO")   # Print NO otherwise

# Execute the main function
main()
