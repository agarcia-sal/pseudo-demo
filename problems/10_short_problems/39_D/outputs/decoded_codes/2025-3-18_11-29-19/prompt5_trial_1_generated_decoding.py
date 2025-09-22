def main():
    # Prompt the user for the first set of values
    print("Enter first set of values:")
    first_set_input = input()

    # Prompt the user for the second set of values
    print("Enter second set of values:")
    second_set_input = input()

    # Split the input strings into separate integer values
    first_set = list(map(int, first_set_input.split()))
    second_set = list(map(int, second_set_input.split()))

    # Initialize a counter for the number of differing values
    difference_count = 0 

    # Loop through the indices of both sets
    for index in range(3):
        # Compare the corresponding values in both sets
        value_from_first_set = first_set[index]
        value_from_second_set = second_set[index]
        
        # If the values are different, increase the count of differences
        if value_from_first_set != value_from_second_set:
            difference_count += 1

    # Check the number of differences counted
    if difference_count < 3:
        # If fewer than 3 differences, print "YES"
        print("YES")
    else:
        # If 3 or more differences, print "NO"
        print("NO")

# Execution starts here
main()
