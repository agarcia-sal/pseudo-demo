# Define a function to find the appropriate index
def find_index():
    # Step 2: Get input and store its absolute value
    target_sum = abs(int(input()))

    # Step 3: Initialize index
    index = 0

    # Step 4: Repeat indefinitely
    while True:
        # Step 4a: Calculate the sum of the first index natural numbers
        current_sum = (index * (index + 1)) // 2

        # Step 4b: Calculate the difference
        difference = current_sum - target_sum

        # Step 4c: Check if current_sum equals target_sum
        if current_sum == target_sum:
            print(index)
            break

        # Step 4d: Check if current_sum is greater than target_sum
        if current_sum > target_sum:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)
                break

        # Step 4e: Increment index
        index += 1

# Call the function
find_index()
