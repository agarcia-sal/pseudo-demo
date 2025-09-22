def main():
    # Read inputs: total items, another quantity, and maximum items per group
    totalItems = int(input())
    anotherQuantity = int(input())
    maxItemsPerGroup = int(input())

    # Calculate the final result by calling the helper function for both totalItems and anotherQuantity
    result = calculateGroups(totalItems, maxItemsPerGroup) * calculateGroups(anotherQuantity, maxItemsPerGroup)

    # Output the calculated result
    print(result)

def calculateGroups(itemCount, itemsPerGroup):
    # Determine how many complete groups can be formed and any remaining items
    numberOfFullGroups, remainingItems = divmod(itemCount, itemsPerGroup)

    # If there are remaining items, return the total items in those groups
    if remainingItems > 0:
        return remainingItems * (numberOfFullGroups + 1)
    else:
        # If there are no remaining items, return the original itemCount
        return itemCount
