def calculateContainers(totalQuantity, containerCapacity):
    fullContainers = totalQuantity // containerCapacity  # Integer division
    remainingItems = totalQuantity % containerCapacity  # Modulus operation
    if remainingItems > 0:
        return fullContainers + 1  # Account for remaining items
    else:
        return fullContainers  # No additional container needed

# Start of the main program
line = input()  # Read line of input
totalGoods, goodsToPack, containerCapacity = map(int, line.split())  # Split and convert to integers

containersForTotalGoods = calculateContainers(totalGoods, containerCapacity)  # Calculate containers needed for total goods
containersForGoodsToPack = calculateContainers(goodsToPack, containerCapacity)  # Calculate containers needed for goods to pack

totalContainers = containersForTotalGoods * containersForGoodsToPack  # Calculate total containers needed

print(totalContainers)  # Output the total number of containers
