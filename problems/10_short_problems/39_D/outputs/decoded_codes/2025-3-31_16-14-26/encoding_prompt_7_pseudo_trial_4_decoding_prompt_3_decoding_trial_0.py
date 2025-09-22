def evaluate_differences_between_inputs():
    # Read two input strings representing sequences of numbers
    first_sequence = input()
    second_sequence = input()
    
    # Split the input strings into lists of strings
    first_list = first_sequence.split()
    second_list = second_sequence.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert the string elements to integers
        number_from_first_list = int(first_list[index])
        number_from_second_list = int(second_list[index])

        # Check if the two numbers are not equal
        if number_from_first_list != number_from_second_list:
            # Increment the difference count
            difference_count += 1

    # If the number of differences is less than 3, output "YES"
    if difference_count < 3:
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Start execution of the program
if __name__ == "__main__":
    evaluate_differences_between_inputs()
