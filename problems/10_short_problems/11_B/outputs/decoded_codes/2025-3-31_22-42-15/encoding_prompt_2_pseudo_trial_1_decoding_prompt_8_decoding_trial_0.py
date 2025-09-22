# Start by getting a number from the user
targetNumber = abs(int(input()))

# Initialize a counter variable
index = 0

# Enter an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    sumOfFirstIndex = (index * (index + 1)) // 2
    # Calculate the difference
    difference = sumOfFirstIndex - targetNumber

    # Check if the current sum equals the target number
    if sumOfFirstIndex == targetNumber:
        print(index)
        break

    # Check if the current sum exceeds the target number
    if sumOfFirstIndex > targetNumber:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(index)
            break

    # Increment the counter variable
    index += 1


def find_index_for_target(target):
    target = abs(target)
    index = 0
    while True:
        sum_of_first_index = (index * (index + 1)) // 2
        difference = sum_of_first_index - target
        if sum_of_first_index == target:
            return index
        if sum_of_first_index > target and difference % 2 == 0:
            return index
        index += 1

# Example usage
target_number = int(input())
print(find_index_for_target(target_number))
