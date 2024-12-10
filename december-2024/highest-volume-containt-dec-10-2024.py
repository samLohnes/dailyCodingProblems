

def maxArea(height):
    left = 0
    right = len(height) - 1
    maxArea = -1
    while left < right:
        length = right - left
        if height[left] > height[right]:
            width = height[right]
            right -=1
        else:
            width = height[left]
            left += 1
        
        maxArea = max(maxArea, length * width)
    return maxArea


print(maxArea([1,8,6,2,5,4,8,3,7]))

print(maxArea([1,1]))
