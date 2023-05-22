def largestRectangleArea(heights):
    # stack holds indexes of increasing bars
    stack = [-1]
    # max_area holds the maximum area so far
    max_area = 0

    for i in range(len(heights)):
        # Pop from stack while top of stack is greater than current bar.
        # On each pop, we calculate the area of rectangle between popped bar
        # and current bar.
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)

        # Append current bar index to stack
        stack.append(i)

    # On exit from loop, pop remaining bars and calculate rectangles with them
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


def largest_rectangle_in_histogram(heights):
    n = len(heights)
    if n == 0:
        return 0

    # Use a stack to keep track of increasing sub-sequences of bars
    stack = []

    # Initialize the maximum area seen so far to 0
    max_area = 0

    # Iterate through the bars in the histogram
    for i in range(n):
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:
            # If the height of the current bar is less than the height of the
            # top bar in the stack, pop the top bar and compute the area of
            # the largest rectangle that can be formed using the height of
            # the popped bar and the width of the sub-sequence of bars to its left
            # print(f'i is {i}, stack is {stack}, stack[-1] is {stack[-1]}')
            idx = stack.pop()
            # print(f'length of stack is {len(stack)}')
            width = i if len(stack) == 0 else i - stack[-1] - 1
            area = heights[idx] * width
            max_area = max(max_area, area)

        # Push the index of the current bar onto the stack
        stack.append(i)
        # print(f'after append is {stack}')

    # Process any remaining bars left in the stack
    while len(stack) > 0:
        idx = stack.pop()
        width = n if len(stack) == 0 else n - stack[-1] - 1
        area = heights[idx] * width
        max_area = max(max_area, area)

    # Return the maximum area seen so far
    return max_area


heights = [2, 1, 5, 6, 2, 3]

print(largest_rectangle_in_histogram(heights))
