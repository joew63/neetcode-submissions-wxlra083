class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # holds indices, heights at these indices are increasing
        largest = 0

        for i, h in enumerate(heights + [0]):  # sentinel 0 flushes the stack at the end
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # left boundary is the new top of stack; if empty, rectangle spans from 0
                left = stack[-1] + 1 if stack else 0
                width = i - left
                largest = max(largest, height * width)
            stack.append(i)

        return largest