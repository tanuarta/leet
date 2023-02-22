# https://leetcode.com/problems/climbing-stairs

# MANUAL CALCULATIONS
# climb(3) = 3
# climb(4) = 5
# climb(5) = 8
# climb(6) = 13

# Initial was basic recursion
# Could not pass LeetCode tests, took too long.
# Realised that recalculations were being done.
# Used memoization
# Time Complexity = O(n)

numDict = {}

def climbDict(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
    
  if n in numDict:  
    res = numDict[n]
  else:
    res = climbDict(n - 1) + climbDict(n - 2)
    numDict[n] = res  
  
  return res

def main():
  n = 38
  
  print(climbDict(n))

if __name__ == "__main__":
  main()