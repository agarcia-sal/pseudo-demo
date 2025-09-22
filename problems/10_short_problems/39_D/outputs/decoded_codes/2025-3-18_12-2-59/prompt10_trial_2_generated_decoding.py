def main():
    # Initialize variables
    input_t1 = input()
    input_t2 = input()
    result = 0

    # Split input strings into lists of integers
    list_t1 = list(map(int, input_t1.split()))
    list_t2 = list(map(int, input_t2.split()))

    # Compare the elements of the lists
    for index in range(3):
        if list_t1[index] != list_t2[index]:
            result += 1

    # Check the result and print
    if result < 3:
        print("YES")
    else:
        print("NO")

# Start execution of the program
if __name__ == "__main__":
    main()


    1 2 3
    1 2 3
    

    1 2 3
    4 5 6
    

    1 2 3
    1 5 3
    