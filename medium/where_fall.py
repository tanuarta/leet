# https://leetcode.com/problems/where-will-the-ball-fall
# Time Complexity = O(m + n)

def fall(grid, row, column):
  while row != len(grid):
    if grid[row][column] == 1:
      if column + 1 == len(grid[0]) or grid[row][column + 1] == -1:
        return -1
      else:
        row += 1
        column += 1
    else:
      if grid[row][column - 1] == 1 or column - 1 == -1:
        return -1
      else:
        row += 1
        column -= 1
  return column
  
def findBall(grid):
  res = []
  for x in range(0, len(grid[0])):
    res.append(fall(grid, 0, x))

  return res

def main():
  grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
  print(findBall(grid))

if __name__ == "__main__":
  main()