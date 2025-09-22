def main_program():
    # Step 1: Gather input from the user
    first_set = input()
    second_set = input()

    # Step 2: Split the input strings into lists of numbers
    first_numbers = first_set.split()
    second_numbers = second_set.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare the numbers in both sets
    for index in range(3):
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])
        
        # If the numbers are different, increase the difference counter
        if first_number != second_number:
            difference_count += 1

    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main_program()
