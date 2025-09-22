def main_program():
    # Step 1: Read two lines of input
    first_set = input()  # User inputs first set of numbers
    second_set = input()  # User inputs second set of numbers

    # Step 2: Split the input strings into lists of numbers
    list_first = first_set.split()  # Split into a list of string numbers
    list_second = second_set.split()  # Split into another list of string numbers

    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter for the number of differences

    # Step 4: Compare each number in the two lists
    for index in range(3):  # We know that there are exactly 3 numbers to compare
        # Convert the current numbers from strings to integers
        number_from_first = int(list_first[index])  # Convert first set's number to integer
        number_from_second = int(list_second[index])  # Convert second set's number to integer

        # Check if the numbers are different
        if number_from_first != number_from_second:  # Compare the two numbers
            difference_count += 1  # Increment the difference counter if they are different

    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO" if differences are 3 or more

# Step 6: Execute the main program
if __name__ == "__main__":
    main_program()
