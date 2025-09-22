def main():
    # Read input values for two test cases
    test_case_1 = input()
    test_case_2 = input()

    # Split the input strings into lists of values
    values_1 = test_case_1.split()  # Split by spaces into a list
    values_2 = test_case_2.split()  # Split by spaces into a list

    # Initialize a counter for differences
    difference_count = 0 

    # Compare corresponding elements from the two lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert string values to integers
        value_1 = int(values_1[index])  # Convert to integer
        value_2 = int(values_2[index])  # Convert to integer

        # Check if the values are different
        if value_1 != value_2:  # Compare the integer values
            difference_count += 1  # Increment the difference counter

    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences output "YES"
    else:
        print("NO")   # 3 or more differences output "NO"

# Execute the main function when the program starts
main()
