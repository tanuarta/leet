# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Time Complexity = O((m + n) log(m)) for both solutions

import math
import bisect

# Finds lowest index that is higher than target
def binary_search(nums, target):
  numSize = len(nums)
  res = math.floor(numSize / 2)
  tmp = 0
  prev = -1
  
  while True:
    if prev == res:
      if nums[res] < target and res != len(nums) - 1 and nums[res + 1] >= target:
        res += 1
        break
      else:
        res = -1
        break
    else:
      prev = res

    if nums[res] >= target:
      numSize = res
      res = math.floor((tmp + res) / 2)
    else:
      tmp = res
      res = math.floor((res + numSize) / 2)
  
  return res

# Original solution with custom binary search
def successfulPairs(spells, potions, success):
  res = []
  potions.sort()

  for spell in spells:
    threshold = math.floor(success / spell)
    found = binary_search(potions, threshold)

    if found == -1:
      res.append(0)
    else:
      res.append(len(potions) - found)

  return res


# Better solution, same algorithm but somehow faster with built-in binary search
# Uses bisect library
def successfulPairsUpgraded(spells, potions, success):
  res = []
  potions.sort()

  for spell in spells:
    threshold = math.floor(success / spell)

    found = bisect.bisect_right(potions,threshold)

    res.append(len(potions) - found)

  return res

def main():
  spells = [3,1,2]
  potions = [8,5,8]
  success = 16

  print(successfulPairs(spells, potions, success))

if __name__ == "__main__":
  main()