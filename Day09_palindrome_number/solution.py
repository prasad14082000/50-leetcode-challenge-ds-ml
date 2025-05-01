# Write your solution here
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
