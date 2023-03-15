# https://leetcode.com/problems/happy-number
# Time Complexity = O(??)

visited = {}

def isHappy(n):
  if n in visited:
    return False
  else:
    visited[n] = 1
  
  digitArray = str(n)
  sum = 0
  
  for num in digitArray:
    sum += int(num) * int(num)


  print(f'sum = {sum}')
  if n == sum:
    if sum == 1:
      return True
    else:
      return False
  else:
    return isHappy(sum)

def main():
  n = 10

  print(isHappy(n))

if __name__ == "__main__":
  main()