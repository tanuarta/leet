# https://leetcode.com/problems/binary-search
from math import floor

def binary_search(nums, target):
  numSize = len(nums)
  res = floor(numSize / 2)
  tmp = 0
  prev = -1
  
  while nums[res] != target:
    if prev == res:
      res = -1
      break
    else:
      prev = res
    if nums[res] > target:
      numSize = res
      res = floor((tmp + res) / 2)
    else:
      tmp = res
      res = floor((res + numSize) / 2)
  
  return res

def main():
  nums = [5]
  target = 5
  print(binary_search(nums, target))

if __name__ == "__main__":
  main()