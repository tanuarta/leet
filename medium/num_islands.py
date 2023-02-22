# https://leetcode.com/problems/number-of-islands
# Time Complexity = O(n+m)

visited = {}

def checkIsland(row, column, grid):
  visited[(row, column)] = 1
  if grid[row][column] == '0':
    return 0
  print(f'row = {row} and column = {column}')
  
  if column < len(grid[row]) - 1 and grid[row][column + 1] == '1' and (row, column + 1) not in visited:
    print('enter right')
    checkIsland(row, column + 1, grid)
  
  if column > 0 and grid[row][column - 1] == '1' and (row, column - 1) not in visited:   
    print('enter left')
    checkIsland(row, column - 1, grid)
  
  if row < len(grid) - 1 and grid[row + 1][column] == '1' and (row + 1, column) not in visited:
    print('enter bottom')
    checkIsland(row + 1, column, grid)
  
  if row > 0 and grid[row - 1][column] == '1' and (row - 1, column) not in visited:
    print('enter top')
    checkIsland(row - 1, column, grid)
  
  return 1

def numIslands(grid):
  sum = 0
  
  for i, row in enumerate(grid):
    for j, column in enumerate(row):
      tup = (i, j)
      if tup not in visited:
        sum += checkIsland(i, j, grid)

  return sum

def main():
  grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

  print(numIslands(grid))

if __name__ == "__main__":
  main()