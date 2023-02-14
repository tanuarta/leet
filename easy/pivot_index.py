# https://leetcode.com/problems/find-pivot-index
# Time Complexity = O(2n) = O(n)

def pivot(arr):

  prevSum = 0
  res = -1
  
  totalSum = 0

  for num in arr:
    totalSum += num

  for i, num in enumerate(arr):
    totalSum -= num
    if prevSum == totalSum:
      return i
    else:
      prevSum += num

  return res

def main():
  arr = [2, 1, -1]
  
  print(pivot(arr))

if __name__ == "__main__":
  main()