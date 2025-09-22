def do_main():
    # Read input for two sets of values
    t1 = input()
    t2 = input()

    # Split the input strings into lists of values
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Compare the corresponding elements of the two lists
    for i in range(3):
        value_a = int(tt1[i])
        value_b = int(tt2[i])

        # If values are not equal, increase the difference counter
        if value_a != value_b:
            difference_count += 1 

    # Determine if the count of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution point
if __name__ == "__main__":
    do_main()
