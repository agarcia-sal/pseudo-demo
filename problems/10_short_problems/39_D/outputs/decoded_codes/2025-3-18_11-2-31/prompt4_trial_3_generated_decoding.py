def do_main():
    # Read two lines of input
    input1 = input()
    input2 = input()

    # Split input strings into lists of components
    split_input1 = input1.split()
    split_input2 = input2.split()

    # Initialize a counter for differences
    differences = 0

    # Compare corresponding elements of the two lists
    for i in range(3):  # Assuming we want to compare the first three elements
        # Convert list elements to integers
        a = int(split_input1[i])
        b = int(split_input2[i])
        # Count differences
        if a != b:
            differences += 1

    # Determine and print the result based on the count of differences
    if differences < 3:
        print("YES")
    else:
        print("NO")


# Main execution starts here
do_main()


  1 2 3
  1 2 4
  

  5 6 7
  5 6 8
  

  10 20 30
  10 20 30
  