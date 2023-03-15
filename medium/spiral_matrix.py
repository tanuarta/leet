# https://leetcode.com/problems/spiral-matrix
# Time Complexity = O(n + m)

visited = {}

def right(matrix, x, y, res):
  if (x, y) in visited:
    y -= 1
    return res, x, y
  
  if y == len(matrix[0]):
    y -= 1
    return res, x, y
  
  print(f'In Right = {(x,y)}')
  
  visited[(x, y)] = 1
  res.append(matrix[x][y])
  
  return right(matrix, x, y + 1, res)
  
def down(matrix, x, y, res):
  if (x, y) in visited:
    x -= 1
    return res, x, y
  
  if x == len(matrix):
    x -= 1
    return res, x, y
  
  print(f'In Down = {(x,y)}')
  
  visited[(x, y)] = 1
  res.append(matrix[x][y])
  
  return down(matrix, x + 1, y, res)
  
def left(matrix, x, y, res):
  if (x, y) in visited:
    y += 1
    return res, x, y
    
  if y == -1:
    y += 1
    return res, x, y
  
  print(f'In left = {(x,y)}')
  visited[(x, y)] = 1
  res.append(matrix[x][y])
  
  return left(matrix, x, y - 1, res)
  
def up(matrix, x, y, res):
  if (x, y) in visited:
    x += 1
    return res, x, y
  
  if x == -1:
    x += 1
    return res, x, y
  
  print(f'In Up = {(x,y)}')
  visited[(x, y)] = 1
  res.append(matrix[x][y])
  
  return up(matrix, x - 1, y, res)

def spiralOrder(matrix):
  
  res = []
  
  maxRow = len(matrix)
  maxColumn = len(matrix[0])
  
  x = 0
  y = 0
  
  while len(res) != maxColumn * maxRow:
    print(res)
    print(visited)
    print(f'going right from {x, y}')
    res, x, y = right(matrix, x, y, res)
    x += 1
    print(f'going down from {x, y}')
    res, x, y = down(matrix, x, y, res)
    y -= 1
    print(f'going left from {x, y}')
    res, x, y = left(matrix, x, y, res)
    x -= 1
    print(f'going up from {x, y}')
    res, x, y = up(matrix, x, y, res)
    print(f'restarting {x,y}')
    y += 1
    
  return res

def main():
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  
  print(spiralOrder(matrix))

if __name__ == "__main__":
  main()