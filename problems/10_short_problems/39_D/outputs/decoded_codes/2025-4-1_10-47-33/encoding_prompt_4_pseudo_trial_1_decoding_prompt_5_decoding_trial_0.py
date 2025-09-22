def main():
    # Read input values
    t1 = input()
    t2 = input()

    # Split the input strings into lists of words
    list1 = t1.split()
    list2 = t2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string values to integers
        a = int(list1[index])
        b = int(list2[index])
        
        # Count differences
        if a != b:
            difference_count += 1

    # Determine output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
