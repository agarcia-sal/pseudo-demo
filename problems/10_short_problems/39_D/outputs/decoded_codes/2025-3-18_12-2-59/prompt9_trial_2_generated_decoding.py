def MainProgram():
    # Input Handling
    first_set_input = input()
    second_set_input = input()

    # Data Preparation
    FirstSet = first_set_input.split()
    SecondSet = second_set_input.split()

    # Initialize a Counter
    differenceCount = 0

    # Comparison Loop
    for index in range(3):  # Looping over the three numbers at indices 0, 1, and 2
        numberFromFirst = int(FirstSet[index])
        numberFromSecond = int(SecondSet[index])
        
        if numberFromFirst != numberFromSecond:
            differenceCount += 1  # Increment the count if they are different

    # Decision Making
    if differenceCount < 3:
        print("YES")  # Output if the sets differ in fewer than three positions
    else:
        print("NO")   # Output if the sets differ in three or more positions

# Execute the Main Program
if __name__ == "__main__":
    MainProgram()
