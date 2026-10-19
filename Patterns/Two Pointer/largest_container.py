# You are given an array of numbers, each representing the height of a vertical line on a graph,
# A container can be formed with any pair of these lines, along with the x-axis o'f the graph,
# Return the amount of water which the largest container can hold.


arr = [2, 7, 8, 3, 7, 6]


def brute_force(arr):
    max_water = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            water_it_can_hold = min(arr[i], arr[j]) * (j - i)
            if max_water < water_it_can_hold:
                max_water = water_it_can_hold
                lines = arr[i], arr[j], j-i

    return max_water, lines


def largest_container_pointer(heights):
    max_water = 0

    # we know the container with max width will hold th max water
    # so start with the edges
    left, right = 0, len(arr)-1

    while left != right:
        # height x width
        water = min(heights[left],heights[right]) * (right - left)
        max_water = max(max_water,water)
        if heights[left] < heights[right]:
            left += 1
        elif heights[right] < heights[left]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_water

if __name__ == "__main__":
    print(brute_force(arr))
    print(largest_container_pointer(arr))
