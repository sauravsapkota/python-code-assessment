from collections import deque


def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()  # Queue to hold the rotten oranges
    fresh_count = 0  # Count of fresh oranges

    # Initialize the queue with all initially rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # Add rotten orange with its time (minute 0)
            elif grid[r][c] == 1:
                fresh_count += 1

    # Directions for the 4-adjacent cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    minutes = 0  # Track the time taken to rot all oranges

    while queue:
        x, y, minutes = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the adjacent cell is a fresh orange
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                grid[nx][ny] = 2  # Mark it as rotten
                fresh_count -= 1  # Decrease the fresh orange count
                queue.append((nx, ny, minutes + 1))  # Add to queue with updated time

    # If there are still fresh oranges, return -1
    return -1 if fresh_count > 0 else minutes


# Example usage
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(oranges_rotting(grid))
