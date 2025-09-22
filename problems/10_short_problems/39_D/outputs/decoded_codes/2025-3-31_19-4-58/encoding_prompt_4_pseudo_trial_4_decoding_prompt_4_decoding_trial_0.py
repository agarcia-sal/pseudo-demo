def main():
    # Read input values
    t1 = input()  # First string input
    t2 = input()  # Second string input

    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize the result counter
    difference_count = 0 

    # Compare the first three elements of both lists
    for index in range(3):
        a = int(tt1[index])
        b = int(tt2[index])
        if a != b:
            difference_count += 1

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
