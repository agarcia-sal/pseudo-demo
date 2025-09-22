def do_main():
    # Read input values for two lists of numbers
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of elements
    list1 = t1.split()
    list2 = t2.split()
    
    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the first three elements of both lists
    for i in range(3):
        # Convert string elements to integers
        num1 = int(list1[i])
        num2 = int(list2[i])

        # If the elements are different, increment the difference counter
        if num1 != num2:
            difference_count += 1

    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
