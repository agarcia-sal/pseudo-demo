# Initialize Variables
n = abs(int(input()))
i = 0

# Start Infinite Loop
while True:
    # Calculate the Sum
    s = (i * (i + 1)) // 2

    # Calculate the Difference
    m = s - n

    # Check for Match
    if s == n:
        print(i)
        break

    # Check for Exceeding Value
    if s > n:
        if m % 2 == 0:
            print(i)
            break

    # Increment Loop Counter
    i += 1


# Initialize Variables
n = abs(int(input()))
i = 0
results = []

# Start Infinite Loop
while True:
    # Calculate the Sum
    s = (i * (i + 1)) // 2

    # Calculate the Difference
    m = s - n

    # Check for Match
    if s == n:
        results.append(i)

    # Check for Exceeding Value
    if s > n:
        if m % 2 == 0:
            results.append(i)
            break

    # Increment Loop Counter
    i += 1

# Print all results
for result in results:
    print(result)
