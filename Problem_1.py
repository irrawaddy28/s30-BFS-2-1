'''
994 Rotting Oranges
https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

1. BFS of undirected graph:
Perform level order traversal where each level is a unit of time. Return the no. of levels (time) after all oranges have rot.
Time: O(MN), Space: O(MN)

Key takeway: This is different from Game of Life problem because this problem has ca onnected components type of situation. This means when a new orange rots in a cell, it affects the oranges in the neighboring cell. Those neighboring cells, in turn, affect their neighboring cells and so on.

'''
from collections import deque

def oranges_rotting(grid):
    assert 10 >= len(grid) >= 1
    assert 10 >= len(grid[0]) >= 1

    deltas = [[-1,0],[1,0],[0,-1],[0,1]] # U, D, L, R
    M = len(grid)
    N = len(grid[0])
    fresh = 0
    q = deque()
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                fresh += 1

            if grid[i][j] == 2:
                q.append(((i,j)))
    if fresh == 0:
        return 0
    time = -1
    # why time = -1? since after popping all level 0 nodes (ewhich happens at the end of first iteration of while loop), we increment time by 1 to get time = 0. Level 0 nodes define the state of the grid at the beginning. Since no time has elapsed at the beginning, we set time=0 after the end of first iteration
    while q:
        K = len(q)
        for _ in range(K):
            curr = q.popleft()
            for delta in deltas:
                x_, y_ = curr[0] + delta[0], curr[1] + delta[1]
                if 0 <= x_ <= M-1 and 0 <= y_ <= N-1:
                    if grid[x_][y_] == 1:
                       q.append((x_,y_))
                       grid[x_][y_] = 2
                       fresh -= 1
        time += 1

    if fresh != 0:
        return -1
    return time

def run_oranges_rotting():
    tests = [ ([[2,1,1],[1,1,0],[0,1,1]],4),
              ([[2,1,1],[0,1,1],[1,0,1]],-1),
              ([[2,1,1],[1,1,1],[0,1,2]],2),
              ([[0,2]],0),
              ([[1]],-1),
              ([[0]],0),
              ([[0,2,2]],0),
    ]
    for test in tests:
        grid, ans = test[0], test[1]
        print(f"\nGrid (original) = {grid}")
        steps = oranges_rotting(grid)
        print(f"Grid (after BFS) = {grid}")
        print(f"Time taken to rot all oranges = {steps}")
        print(f"Pass: {ans == steps}")

run_oranges_rotting()