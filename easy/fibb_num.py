# https://leetcode.com/problems/fibonacci-number
# O(n^3)

def fib(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
    
  sum = fib(n - 1) + fib(n - 2)
  
  return sum

def main():
  n = 6
  print(fib(n))

if __name__ == "__main__":
  main()
  
# Came back after climbing stairs
# Improved version
# Time Complexity = O(n)

numDict = {}

def fibImproved(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
    
  if n in numDict:
    sum = numDict[n]
  else:
    sum = fib(n - 1) + fib(n - 2)
    numDict[n] = sum
  
  return sum