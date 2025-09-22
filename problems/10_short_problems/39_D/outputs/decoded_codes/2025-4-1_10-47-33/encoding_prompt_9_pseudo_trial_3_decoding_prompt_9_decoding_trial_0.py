# Main function to compare two sets of integers
def main():
    # Step 1: Read the first set of integers from the user
    print("Enter the first set of three integers:")
    first_set = input()  # Read user input

    # Step 2: Read the second set of integers from the user
    print("Enter the second set of three integers:")
    second_set = input()  # Read user input

    # Step 3: Split the input strings into lists of integers
    first_list = first_set.split()  # Split input string into list
    second_list = second_set.split()  # Split input string into list

    # Step 4: Initialize a counter for the differences
    difference_count = 0

    # Step 5: Compare the corresponding integers from both lists
    for index in range(3):  # Loop through the first three elements
        # Convert strings to integers for comparison
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1

    # Step 6: Determine output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to run the program
main()
