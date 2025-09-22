def main():
    # Step 1: Read the first set of integers from the user
    print("Enter the first set of three integers:")
    first_set = input()  # Read user input

    # Step 2: Read the second set of integers from the user
    print("Enter the second set of three integers:")
    second_set = input()  # Read user input

    # Step 3: Split the input strings into lists of integers
    first_list = first_set.split()  # Split input into individual numbers
    second_list = second_set.split()  # Split input into individual numbers

    # Step 4: Initialize a counter for differences
    difference_count = 0

    # Step 5: Compare the corresponding integers from both lists
    for index in range(3):  # Looping through each of the three integers
        # Convert string to integer for comparison
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer
        
        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1  # Increment difference count

    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")  # 3 or more differences

# Call the main function to execute the program
main()
