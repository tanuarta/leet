# https://leetcode.com/problems/flood-fill
# Time Complexity = O(n+m)

def rec(image, sr, sc, color, base, maxRow, maxColumn):
  if image[sr][sc] != base:
    return image
  
  if image[sr][sc] == color:
    return image
  else:
    image[sr][sc] = color
  
  if sr + 1 != maxRow: image = rec(image, sr + 1, sc, color, base, maxRow, maxColumn)
  if sc + 1 != maxColumn: image = rec(image, sr, sc + 1, color, base, maxRow, maxColumn)
  if sr - 1 != -1: image = rec(image, sr - 1, sc, color, base, maxRow, maxColumn)
  if sc - 1 != -1: image = rec(image, sr, sc - 1, color, base, maxRow, maxColumn)

  return image

def floodFill(image, sr, sc, color):
  base = image[sr][sc]
  maxRow = len(image)
  maxColumn = len(image[1])
  
  return rec(image, sr, sc, color, base, maxRow, maxColumn)

def main():
  arr = [[0,0,0],[0,0,0]]
  sr = 0
  sc = 0
  color = 0

  print(floodFill(arr, sr, sc, color))

if __name__ == "__main__":
  main()