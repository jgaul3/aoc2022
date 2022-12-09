import numpy as np


def get_visible(filename: str):
    with open(filename) as file:
        heights = np.array([list(map(int, list(line.strip()))) for line in file])

    count = 2 * heights.shape[0] + 2 * heights.shape[1] - 4
    for x in range(1, heights.shape[0] - 1):
        for y in range(1, heights.shape[1] - 1):
            current_height = heights[x][y]
            if (
                current_height > heights[x, :y].max()
                or current_height > heights[x, y + 1:].max()
                or current_height > heights[:x, y].max()
                or current_height > heights[x + 1:, y].max()
            ):
                count += 1

    scores = np.zeros_like(heights)
    for (x, y), curr_height in np.ndenumerate(heights):
        up_offset = down_offset = left_offset = right_offset = 1
        while x - up_offset > 0 and heights[x - up_offset, y] < curr_height:
            up_offset += 1
        while x + down_offset < heights.shape[0] - 1 and heights[x + down_offset, y] < curr_height:
            down_offset += 1
        while y - left_offset > 0 and heights[x, y - left_offset] < curr_height:
            left_offset += 1
        while y + right_offset < heights.shape[1] - 1 and heights[x, y + right_offset] < curr_height:
            right_offset += 1
        scores[x, y] = up_offset * down_offset * left_offset * right_offset
    return count, np.max(scores[1:-1, 1:-1])


if __name__ == "__main__":
    print(get_visible("input0.txt"))
    print(get_visible("input1.txt"))
