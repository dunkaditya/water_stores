# we start with a simple solution, just finding the left and right bound
# at every building, this is O(n^2)!
def water_stored_basic(height):
    sol = 0
    for i in range(1, len(height)-1):
        # find the left bound
        left = height[i]
        for j in range(0, i):
            if(height[j] > left):
                left = height[j]

        # this means we are at a peak
        if left == height[i]:
            # print("skipped")
            continue

        # find the right bound
        right = height[i]
        for j in range(i+1, len(height)):
            if(height[j] > right):
                right = height[j]

        # this means we are at a peak
        if right == height[i]:
            # print("skipped")
            continue

        # print(f"right: {right}, left: {left}, height: {height[i]}")
        water_level = min(right, left)
        sol += (water_level - height[i])
    return sol
    

