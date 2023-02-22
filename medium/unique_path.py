# https://leetcode.com/problems/unique-paths
# Time Complexity = O(m + n)

pathDict = {}

def uniquePaths(m, n):
  if (m, n) in pathDict:
    return pathDict[(m, n)]
    
  if m == 0 and n == 1:
    pathDict[(m, n)] = 1
    return 1
  if m == 1 and n == 0:
    pathDict[(m, n)] = 1
    return 1
  if m == 0 and n == 0:
    return 0
  
  x = 0
  y = 0
  if n > 0:
    x = uniquePaths(m, n - 1)
  if m > 0:
    y = uniquePaths(m - 1, n)

  pathDict[(m, n)] = x + y
  return x + y
  
def main():
  m = 23
  n = 12

  print(uniquePaths(m, n))

if __name__ == "__main__":
  main()