def main():
    # Read two lines of input from the user, representing two sequences of numbers
    first_sequence = input()
    second_sequence = input()

    # Split the input strings into lists of numbers
    first_list = first_sequence.split()
    second_list = second_sequence.split()

    # Initialize a variable to count the number of differences
    difference_count = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements from strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            # Increment the count of differences
            difference_count += 1

    # If the count of differences is less than 3, print "YES", else print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    main()
