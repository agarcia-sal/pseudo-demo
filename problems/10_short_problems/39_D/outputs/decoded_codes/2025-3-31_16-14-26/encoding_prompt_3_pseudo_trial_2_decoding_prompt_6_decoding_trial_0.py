# Define the main function where the program logic will reside
def main():
    # Step 1: Read input from the user
    input_string1 = input()  # Read first input string from the user
    input_string2 = input()  # Read second input string from the user

    # Step 2: Split the input strings into lists of words
    list1 = input_string1.split()  # Create a list from the first input string by splitting
    list2 = input_string2.split()  # Create a list from the second input string by splitting

    # Step 3: Initialize a variable to count differences
    difference_count = 0  # Counter for the number of differences

    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # Loop through the first three indices
        # Convert the current elements to integers
        value_a = int(list1[index])  # Convert the element at index from first list to integer
        value_b = int(list2[index])  # Convert the element at index from second list to integer

        # Step 5: Check if the values are different
        if value_a != value_b:  # If the values at the current index are not equal
            difference_count += 1  # Increment the difference count by 1

    # Step 6: Determine and print if differences are less than 3
    if difference_count < 3:  # Check if the number of differences is less than 3
        print("YES")  # If true, print "YES"
    else:
        print("NO")  # Otherwise, print "NO"

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to execute the program
