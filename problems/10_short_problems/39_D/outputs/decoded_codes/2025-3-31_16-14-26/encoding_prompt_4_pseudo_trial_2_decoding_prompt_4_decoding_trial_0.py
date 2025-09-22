def main():
    # Read two strings of input
    input1 = input()
    input2 = input()

    # Split the input strings into lists of components
    components1 = input1.split()
    components2 = input2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Iterate over the first three components of both lists
    for index in range(3):
        # Convert each component to an integer
        value1 = int(components1[index])
        value2 = int(components2[index])

        # Check if the values are different
        if value1 != value2:
            difference_count += 1 

    # Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start program execution
if __name__ == "__main__":
    main()
