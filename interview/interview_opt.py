# we notice that once we find left and right bound, we only change it when we hit the right bound
def water_stored(height):
    sol = 0
    left = height[0]
    right = -1
    for i in range(1, len(height)-1):

        if height[i] > left:
            left = height[i]

        # if we need to find right bound
        if right == -1:
            right = height[i]
            for j in range(i+1, len(height)):
                if(height[j] >= right):
                    right = height[j]

        # this means we hit our right bound, and need to start over
        if right == height[i]:
            left = height[i]
            right = -1
            # print("skipped")
            continue

        # print(f"left: {left}, right: {right}, height: {height[i]}")
        water_level = min(right, left)
        sol += (water_level - height[i])
    return sol