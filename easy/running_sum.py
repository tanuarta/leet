# https://leetcode.com/problems/running-sum-of-1d-array
# Time Complexity = O(n)

def runningSum(arr):
  
  sum = 0
  res = []
  
  for num in arr:
    sum += num
    res.append(sum)
  
  return res

def main():
  arr = [1, 2, 3, 4]

  print(runningSum(arr))

if __name__ == "__main__":
  main()