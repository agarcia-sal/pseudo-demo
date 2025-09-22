def do_main():
    # Read input strings
    string1 = input()
    string2 = input()

    # Split the input strings into lists of values
    list1 = string1.split()
    list2 = string2.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers
        value_a = int(list1[index])
        value_b = int(list2[index])
        
        # Check if the values are different
        if value_a != value_b:
            difference_count += 1

    # Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution
do_main()
