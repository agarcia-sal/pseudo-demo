def normalizePath(filePath):
    # Implementation that normalizes the path
    # For the purpose of this example, we'll use the os module to normalize
    import os
    nor = os.path.normpath(filePath)
    return nor

def removeExtraLeadingSlashes(filePath):
    # This function ensures that the path starts with exactly one slash
    if filePath.startswith('/'):
        # Remove all leading slashes and then add one back
        modifiedPath = '/' + filePath.lstrip('/')
    else:
        modifiedPath = filePath
    return modifiedPath

# Step 1: Read input from standard input (simulating file path input)
ra = input()

# Step 2: Normalize the file path
nor = normalizePath(ra)

# Step 3: Ensure the path starts with a single forward slash
if nor.startswith('/'):
    red = removeExtraLeadingSlashes(nor)
else:
    red = nor  # If there are no leading slashes, keep it as is

# Step 4: Print the final result
print(red)
