def maxArea(self, height: List[int]) -> int:
    maxArea = 0
    i,j = 0, len(height)-1
    
    while i < j:
        gap = j-i
        minHeight = min(height[i], height[j])
        area = gap * minHeight
        if area > maxArea:
            maxArea = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return maxArea